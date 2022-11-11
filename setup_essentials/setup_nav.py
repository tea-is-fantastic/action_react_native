import os

from actions.action_rn_android import navigation as nav_android


def setup_nav():
    os.system('npm i --save react-navigation react-native-screens, react-native-safe-area-context')
    nav_android()

