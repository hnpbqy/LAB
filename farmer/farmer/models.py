#coding=utf8

import os
import sys
import time
from psutil import Process
from datetime import datetime
from threading import Thread

from ansible.runner import Runner
from ansible.inventory import Inventory

from django.db import models

from farmer.settings import WORKER_TIMEOUT, ANSIBLE_FORKS, ANSIBLE_INVENTORY


class Task(models.Model):

    # hosts, like web_servers:host1 .
    inventory = models.TextField(null = False, blank = False)

    # 0, do not use sudo; 1, use sudo .
    sudo = models.BooleanField(default = True)

    # for example: ansible web_servers -m shell -a 'du -sh /tmp'
    # the 'du -sh /tmp' is cmd here
    cmd = models.TextField(null = False, blank = False)

    # return code of this job
    rc = models.IntegerField(null = True)

    # submitter
    farmer = models.TextField(null = False, blank = False)

    start = models.DateTimeField(null = True, blank = False)
    end = models.DateTimeField(null = True, blank = False)

    def run(self):
        t = Thread(target = self._run)
        t.setDaemon(True)
        t.start()

    def _run(self):
        self.start = datetime.now()
        self.save()

        # initial jobs
        for host in Inventory(ANSIBLE_INVENTORY).list_hosts(self.inventory):
            self.job_set.add(Job(host = host, cmd = self.cmd,
                                 start = datetime.now()))
        self.save()

        runner = Runner(module_name = 'shell', module_args = self.cmd,
                        pattern = self.inventory, sudo = self.sudo,
                        forks = ANSIBLE_FORKS, host_list = ANSIBLE_INVENTORY)

        _, poller = runner.run_async(time_limit = WORKER_TIMEOUT)

        now = time.time()

        while True:

            if poller.completed or time.time() - now > WORKER_TIMEOUT: # TIMEOUT
                break

            results = poller.poll()
            results = results.get('contacted')

            if results:
                for host, result in results.items():
                    job = self.job_set.get(host = host)
                    job.end = result.get('end')
                    job.rc = result.get('rc')
                    job.stdout = result.get('stdout')
                    job.stderr = result.get('stderr')
                    job.save()

            time.sleep(1)

        jobs_timeout = filter(lambda job: job.rc is None, self.job_set.all()) # rc is None
        jobs_failed = filter(lambda job: job.rc, self.job_set.all()) # rc > 0

        for job in jobs_timeout:
            job.rc = 1
            job.stderr = 'JOB TIMEOUT' # marked as 'TIMEOUT'
            job.save()

        self.rc = (jobs_timeout or jobs_failed) and 1 or 0

        self.end = datetime.now()
        self.save()

        self.done()

    def done(self):
        try:
            myself = Process(os.getpid())
            for child in myself.get_children():
                child.kill()
        except Exception as e:
            sys.stderr.write(str(e) + '\n')

    def __unicode__(self):
        return self.cmd + ' @ ' + self.inventory

class Job(models.Model):
    task = models.ForeignKey(Task)
    host = models.TextField(null = False, blank = False)
    cmd = models.TextField(null = False, blank = False)
    start = models.DateTimeField(null = True, blank = False)
    end = models.DateTimeField(null = True, blank = False)
    rc = models.IntegerField(null = True)
    stdout = models.TextField(null = True)
    stderr = models.TextField(null = True)

    def __unicode__(self):
        return self.host + ' : ' + self.cmd
