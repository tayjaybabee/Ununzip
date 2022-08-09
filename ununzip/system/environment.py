"""

File:
    PROJECT_ROOT/ununzip/system/environment.py

Date:
    08/06/2022 - 10:32 hrs

Project:
    Sandbox - Ununzip

Description:
    environment.py holds the EnvironmentVariables class which helps grab and use environment
    variables in a cross-platform manner.

Author:
    Taylor-Jayde Blackstone <t.blackstone@inspyre.tech>

License:
    MIT

"""


from os import environ
from box import Box
import sys


class EnvironmentVariables(object):
    def __init__(self):
        self.__vars = environ.keys()
        self.__true_vals = ['yes',  'y', 'true', 't', 1]
        self.__false_vals = ['no', 'n', 'false', 'f', 0]

    @property
    def box(self):
        return Box(self.var_dict)

    @property
    def vars(self):
        return list(environ.keys())

    @property
    def var_dict(self):
        return dict(environ.items())

    @property
    def environ(self):
        return environ

    def __get(self, *args, **kwargs):
        ignore_boolean = kwargs['ignore_boolean']
        key = args[0]
        
        if self.has_var(key):
            entry = self.environ[key]
            if not ignore_boolean:
                if self.__true_vals in entry.lower():
                    return True
                elif self.__false_vals in entry.lower():
                    return False

            return entry
        else:
            raise KeyError(key)

    def get(self, key, ignore_boolean=False):
        try:
            return self.__get(args, kwargs)
        except KeyError as e:
            print(f'An error occurred: {sys.exc_info()[0]}: {e}')
            return None
            
    @property
    def count(self):
        return len(self.vars)

    def has_var(self, var):
        var = var.upper()
        if var in self.var_dict.keys():
            return True
        else:
            return False
    
