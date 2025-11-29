import os

from config.config_reader import config_parser


BASE_DIR = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

CONFIG = config_parser()


class Utility:

    @staticmethod
    def get_list_from_config(config_item):
        return config_item.replace(" ", "").split(",")