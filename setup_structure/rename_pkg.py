import os

from scripts.tif_yaml import app_yaml


def rename_pkg():
    cmd = f'npx react-native-rename {app_yaml.name} -b {app_yaml.apk}'
    os.system(cmd)
