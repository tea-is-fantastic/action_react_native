import os
import re

from actions.action_react_native.utils import rn_theme
from scripts.tif_util import reg_rep
from scripts.tif_yaml import colors_yaml


def setup_colors():
    os.system(f'npm i -s color')
    code = """import Color from 'color';
    """

    for attr, value in colors_yaml.items():
        if attr == "dark":
            for attrd, valued in value:
                code += f"export const {attrd}ColorDark = Color({valued}).hex()"

        elif attr == "light":
            for attrd, valued in value:
                code += f"export const {attrd}ColorLight = Color({valued}).hex()"

        else:
            code += f"export const {attr}Color = Color({value}).hex()"

    with open(os.path.join(rn_theme, 'colors.ts'), 'w') as f:
        f.write(code)
