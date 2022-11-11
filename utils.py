import os

from scripts.tif_env import TEMP_PATH
from scripts.tif_yaml import app_yaml

rn_path = os.path.join(TEMP_PATH, app_yaml.name)
rn_src = os.path.join(rn_path, 'src')
rn_assets = os.path.join(rn_path, 'assets')
rn_screens = os.path.join(rn_src, 'screens')
rn_components = os.path.join(rn_src, 'components')
rn_theme = os.path.join(rn_src, 'theme')
rn_providers = os.path.join(rn_src, 'providers')
rn_models = os.path.join(rn_src, 'models')
rn_shared = os.path.join(rn_src, 'shared')

all_dirs = [rn_src, rn_assets, rn_screens, rn_components, rn_theme, rn_providers, rn_models, rn_shared]