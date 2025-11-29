from pathlib import Path
import configparser as cp
import os


def config_parser():
    config = cp.ConfigParser(interpolation=None)
    config.read(Path(__file__).parent / 'config_tools.ini')
    return config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__))).replace('\\', '/')
