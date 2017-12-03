import os

from fabric.api import task
from fabric.context_managers import lcd
from fabric.operations import local

root_path = os.getcwd()
app_path = root_path + '/project'

@task
def make():
    with lcd(app_path):
        local('./manage.py makemigrations')

@task
def run():
    with lcd(app_path):
        local('./manage.py migrate')
