"""
Build script
"""

import os
from sys import argv

print("building file name:", argv[1])
os.system(f'flet build apk --no-android-splash --product "{argv[1]}" -vv')
