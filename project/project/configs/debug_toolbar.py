import os

def _parse_debug_toolbar_env(request):
    enable = os.environ.get('DEBUG_TOOLBAR_ENABLED')
    return enable == 'On'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'project.configs.debug_toolbar._parse_debug_toolbar_env',
}
