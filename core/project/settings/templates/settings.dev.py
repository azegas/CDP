"""

Sample settings template file that other developers can use to
override base.py settings file with their own settings. Should be
placed in "local/settings.dev.py file.

/home/arvy/src/CDP/local/settings.dev.py

"""

SECRET_KEY = "secretkey"
DEBUG = True

LOGGING["formatters"]["colored"] = {  # type: ignore
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["core"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore
