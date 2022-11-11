import os
import re

from ..utils import rn_theme
from scripts.tif_util import reg_rep
from scripts.tif_yaml import app_yaml
from snippets.snippet import app_yaml


def nav_theme():
    with open(os.path.join(rn_theme, 'navigation.ts'), 'w') as f:
        f.write(nav_theme())
    reg_rep(os.path.join(app_yaml, 'MainActivity.java'),
            r'^(public class MainActivity)',
            r'import android.os.Bundle;\n\n\1',
            already='android.os.Bundle')

    reg_rep(os.path.join(android_java, 'MainActivity.java'),
            r'^(public class MainActivity)',
            fr'\1\n\n{code}',
            already='void onCreate')
