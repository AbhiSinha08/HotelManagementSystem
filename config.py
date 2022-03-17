""" File: cfg.py / config.py """
""" To collect and parse data from config files (config.ini and notifications.ini) """

import configparser

cfg = configparser.ConfigParser()


print("Reading config files...")
# Parsing configuration from config.cfg
cfg.read("mysql.cfg")

# MySQL Configuration
HOST = cfg['mysql']['host']
PORT = int(cfg['mysql']['port'])
USER = cfg['mysql']['user']
PASSWORD = cfg['mysql']['password']
DATABASE = cfg['mysql']['db']