import os

from fabric.api import task
from fabric.context_managers import lcd
from fabric.operations import local

root_path = os.getcwd()
app_path = root_path + '/project'

@task
def run(app='memberships.tests'):
    with lcd(app_path):
        local('./manage.py test {} --pattern="*.py"'.format(app))
