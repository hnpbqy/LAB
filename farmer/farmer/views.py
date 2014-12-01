from django.shortcuts import render_to_response, redirect
from django.contrib.admin.views.decorators import staff_member_required

from farmer.models import Task
from farmer.settings import NUMBER_OF_TASK_PER_PAGE

def run_task(request, inventory, cmd):
    task = Task()
    task.inventory = inventory
    task.cmd = cmd
    task.farmer = request.user.username
    task.run()


@staff_member_required
def home(request):
    if request.method == 'POST':
        inventory = request.POST.get('inventory', '')
        cmd = request.POST.get('cmd', '')
        if '' in [inventory.strip(), cmd.strip()]:
            return redirect('/')
        run_task(request, inventory, cmd)
        return redirect('/')
    else:
        tasks = Task.objects.all().order_by('-id')[:NUMBER_OF_TASK_PER_PAGE]
        return render_to_response('home.html', locals())

@staff_member_required
def detail(request, id):
    assert(request.method == 'GET')
    jobid = request.GET.get('jobid', '')
    if jobid.isdigit():
        jobid = int(jobid)
    else:
        jobid = -1
    task = Task.objects.get(id = id)
    #jobs = task.job_set.all().order_by('-rc')
    jobs = task.job_set.all()
    jobs_succeed = [ job for job in jobs if job.rc == 0 ]
    jobs_failed = [ job for job in jobs if job.rc != 0 ]
    jobs = jobs_failed + jobs_succeed
    return render_to_response('detail.html', locals())

@staff_member_required
def retry(request, id):
    assert(request.method == 'GET')
    task = Task.objects.get(id = id)
    failure_hosts = [job.host for job in task.job_set.all() if job.rc != 0]
    assert(failure_hosts)
    inventory = ':'.join(failure_hosts)
    run_task(request, inventory, task.cmd)
    return redirect('/')

@staff_member_required
def rerun(request, id):
    assert(request.method == 'GET')
    task = Task.objects.get(id = id)
    run_task(request, task.inventory, task.cmd)
    return redirect('/')


