import os

from actions.action_rn_android import bootsplash as bs_android
from scripts.tif_util import download
from scripts.tif_yaml import assets_yaml


def gen_icon():
    download(assets_yaml.icon, os.path.join(os.getcwd(), 'icon.svg'))
    cmd = f'npx react-native-svg-app-icon'
    os.system(cmd)


def gen_splash():
    download(assets_yaml.splash, os.path.join(os.getcwd(), "assets", 'bootsplash.png'))
    os.system('npm i --save react-native-bootsplash')
    cmd = f'npx react-native generate-bootsplash assets/bootsplash.png \
  --background-color={assets_yaml.splash_bg} \
  --logo-width=100 \
  --assets-path=assets \
  --flavor=main'
    os.system(cmd)
    bs_android()


def gen_assets():
    gen_icon()
    gen_splash()
