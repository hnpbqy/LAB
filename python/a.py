from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()


def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'


displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2 + 1.9j)
displayNumType('xxx')

#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
inp = raw_input('Identifier to test? ')

if len(inp) > 1:

    if inp[0] not in alphas:
        print '''invalid: first symbol must be
	  alphabetic'''
    else:
        for otherChar in inp[1:]:

            if otherChar not in alphas + nums:
                print '''invalid: remaining
		  symbols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"

#!/usr/bin/env python

queue = []


def enQ():
    queue.append(raw_input('Enter new queue element: '))


def deQ():
    if len(queue) == 0:
        print 'Cannot dequeue from empty queue!'
    else:
        print 'Removed [', queue.pop(0), ']'


def viewQ():
    print str(queue)


def showmenu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'devq':
                print 'invalid option, try again'
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'e': enQ()
        if choice == 'd': deQ()
        if choice == 'v': viewQ()


if __name__ == '__main__':
    showmenu()

#!/usr/bin/env python

db = {}


def newuser():
    prompt = 'login desired: '
    while 1:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = pwd


def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        pass
    else:
        print 'login incorrect'
        return

    print 'welcome back', name


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            if choice not in 'neq':
                print 'invalid menu option, try again'
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()


if __name__ == '__main__':
    showmenu()

#!/usr/bin/env python

import os
for tmpdir in ('/tmp', 'c:/windows/temp'):
    if os.path.isdir(tmpdir):
	break
else:
    print 'no temp directory available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd

    print '*** creating example directory...'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory:'
    print cwd
    print '*** original directory listing:'
    print os.listdir(cwd)

    print '*** creating test file...'
    file = open('test', 'w')
    file.write('foo\n')
    file.write('bar\n')
    file.close()
    print '*** updated directory listing:'
    print os.listdir(cwd)

    print "*** renaming 'test' to 'filetest.txt'"
    os.rename('test', 'filetest.txt')
    print '*** updated directory listing:'
    print os.listdir(cwd)

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print '*** full file pathname:'
    print path
    print '*** (pathname, basename) == '
    print os.path.split(path)
    print '*** (filename, extension) == '
    print os.path.splitext(os.path.basename(path))

    print '*** displaying file contents:'
    file = open(path)
    allLines = file.readlines()
    file.close()
    for eachLine in allLines:
	print eachLine,

    print '*** deleting test file'
    os.remove(path)
    print '*** updated directory listing:'
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print '*** deleting test directory'
    os.rmdir('example')
    print '*** DONE'
