# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import logging

plugins = []


class Plugin(object):
    # __name = 'undefined'

    def __init__(self):
        # if not hasattr(self, '_%s__name' % self.__get_class_name()):
        #     setattr(self, '_%s__name' % self.__get_class_name(), 'undefined')
        #     self.__name = 'undefined'
        # else:
        #     self.__name = getattr(self, '_%s__name' % self.__get_class_name())
        if not hasattr(self, '_name'):
            self._name = 'undefined'
        logging.debug('Plugin "%s" loaded' % self._name)

    @classmethod
    def __get_class_name(cls):
        return cls.__name__

    def __str__(self):
        return '<Plugin %s>' % self._name


def load_plugins(dir_path):
    from os import scandir
    from importlib import import_module
    from sys import path
    path.insert(0, dir_path)
    for entry in scandir(dir_path):
        if not entry.name.startswith('.') and entry.is_file() \
                and entry.name.lower().endswith('.py'):
            m = import_module(entry.name[:-3])
            # for obj_name in dir(m):
            #     if not obj_name.startswith('__'):
            #         obj = getattr(m, obj_name)
            #         # if isinstance(obj, type) and issubclass(obj, Plugin) \
            #         #         and 'Plugin' not in obj_name:
            #         if obj in Plugin.__subclasses__():
            #             p = obj()
            #             plugins.append(p)

    for plugin in Plugin.__subclasses__():
        p = plugin()
        plugins.append(p)

    return plugins
