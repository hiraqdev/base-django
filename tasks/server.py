import os

from fabric.api import task
from fabric.context_managers import lcd
from fabric.operations import local

root_path = os.getcwd()
app_path = root_path + '/project'

@task
def run(ip='0.0.0.0', port='8080'):
    with lcd(app_path):
        local('./manage.py runserver {}:{}'.format(ip, port))
