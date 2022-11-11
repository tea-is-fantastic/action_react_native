import os
from pathlib import Path
from ..utils import rn_path, all_dirs


def create_dirs():
    for d in all_dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
