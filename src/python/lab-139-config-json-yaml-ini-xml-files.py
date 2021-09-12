#
# filename    : lab-139-config-json-yaml-ini-xml-files.py
# Description : configuration files
# Docs        :
#               * https://martin-thoma.com/configuration-files-in-python/
# Requirements:
#

# #############################################################################
# Part I: Python config file 
# #############################################################################

import importlib

cfg = importlib.import_module("file-16-includable-config-file")

print('\nPart I: The simplest way to write configuration files is to simply write a separate file that contains Python code.\n')
print('  * cfg.mysql["host"]                :', cfg.mysql['host'])
print("  * cfg.mysql['user']                :", cfg.mysql['user'])
print("  * cfg.mysql['password']            :", cfg.mysql['password'])
print("  * cfg.mysql['dbname']              :", cfg.mysql['dbname'])
print("  * cfg.mysql['user']                :", cfg.mysql['user'])
print("  * cfg.mysql[('dbname','tablename')]:", cfg.mysql[('dbname','tablename')])
print("  * cfg.mysql['tablenames']          :", cfg.mysql['tablenames'])
print("  * cfg.mysql['tablenames'][0]       :", cfg.mysql['tablenames'][0])
print("  * cfg.mysql['tablenames'][1]       :", cfg.mysql['tablenames'][1])
print("  * cfg.mysql['tables']              :", cfg.mysql['tables'])
print("  * cfg.mysql['tables']['mytable1']  :", cfg.mysql['tables']['mytable1'])
print("  * cfg.mysql['tables']['mytable2']  :", cfg.mysql['tables']['mytable2'])


# #############################################################################
# Part II: JSON
# #############################################################################

import json

print('\nPart II: JSON is short for JavaScript Object Notation. It is widespread and thus has good support for many programming languages.\n')

with open("file-17-config.json") as json_data_file:
    json_data = json.load(json_data_file)
print("* json_data                                             : ", json_data)
print("* json_data['mysql']                                                  : ", json_data['mysql'])
print("* json_data['mysql']['host']                                          : ", json_data['mysql']['host'])
print("* json_data['mysql']['user']                                          : ", json_data['mysql']['user'])
print("* json_data['mysql']['password']                                      : ", json_data['mysql']['password'])
print("* json_data['mysql']['dbname']                                        : ", json_data['mysql']['dbname'])
print("* json_data['mysql']['dbname']['tables']                              : ", json_data['mysql']['dbname']['tables'])
print("* json_data['mysql']['dbname']['tables'][0]                           : ", json_data['mysql']['dbname']['tables'][0])
print("* json_data['mysql']['dbname']['tables'][1]                           : ", json_data['mysql']['dbname']['tables'][1])
print("* json_data['mysql']['dbname']['tables'][2]                           : ", json_data['mysql']['dbname']['tables'][2])
print("* json_data['mysql']['dbname']['tables'][0]['tablename']              : ", json_data['mysql']['dbname']['tables'][0]['tablename'])
print("* json_data['mysql']['dbname']['tables'][0]['columns']                : ", json_data['mysql']['dbname']['tables'][0]['columns'])
print("* json_data['mysql']['dbname']['tables'][0]['columns']['id_column']   : ", json_data['mysql']['dbname']['tables'][0]['columns']['id_column'])
print("* json_data['mysql']['dbname']['tables'][0]['columns']['name_column'] : ", json_data['mysql']['dbname']['tables'][0]['columns']['name_column'])


# #############################################################################
# 
# #############################################################################
