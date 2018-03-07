import os

from fabric.api import task
from fabric.context_managers import lcd
from fabric.operations import local

root_path = os.getcwd()
app_path = root_path + '/project'

@task
def build():
    with lcd(app_path):
        local('npm run build')

@task
def install(package='', saveDev='no'):
    with lcd(app_path):
        saveCommand = '--save'
        if saveDev == 'yes':
            saveCommand = '--save-dev'

        if package != '':
            local('npm install {} {}'.format(saveCommand, package))
        else:
            local('npm install')
