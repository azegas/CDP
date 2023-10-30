import os.path
from pathlib import Path

from split_settings.tools import include, optional

# our base directory, in our case its CDP folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# /home/arvy/src/CDP

# whenever we want a system variable to be pulled in here
# (whether from docker or system you are currently developing on),
# we will have to prefix it with this string below:
ENVVAR_SETTINGS_PREFIX = "CORESETTINGS_"

LOCAL_SETTINGS_PATH = os.getenv(f"{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = "local/settings.dev.py"

# if relative path is found, converting it to absolute path
if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)
    # /home/arvy/src/CDP/local/settings.dev.py

include(
    "base.py",  # base settings that we will use for every environment
    "custom.py",  # cusom config not related to Django
    "logging.py",  # logging config
    optional(LOCAL_SETTINGS_PATH)  # Include if exist. Overrides base.py
)
