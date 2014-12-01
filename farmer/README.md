Farmer
======

an asynchronous task execution app based on ansible

# First Of All !

you should deploy your [ansible](https://github.com/ansible/ansible) cluster

see: http://www.ansibleworks.com/docs/intro_getting_started.html

#Screenshot
![Screenshot](https://raw.github.com/douban/farmer/master/farmer/static/images/farmer-home.png)
![Screenshot](https://raw.github.com/douban/farmer/master/farmer/static/images/farmer-detail.png)

# Running

```
git clone https://github.com/douban/farmer.git
cd farmer
python manage.py syncdb
```

in this step, you should add a user(administrator), just input your name / pass

then run it with:

```
python manage.py runserver 0.0.0.0:6969
```

view it in `http://your-domain:6969`

# Features
* asynchronous task execution with ansible python bindings
* show task / job status in realtime
* `retry` cmd on those failed hosts by a `retry` button
* `rerun` any task
* time out support
