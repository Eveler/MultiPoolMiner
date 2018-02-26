# -*- encoding: utf-8 -*-

# Author: Savenko Mike
from time import sleep

from core.plugin import Plugin


class Cast(Plugin):
    _name = "Cast"
    server = "localhost"
    timeout = 10  # seconds
    delta = 0.05
    interval = 5

    def get_hash_rate(self, algo, safe=False):
        hashrates = []
        while len(hashrates) < 6:
            data = self.get_response()
            value = data['devices']['hash_rate'] / 1000
            hashrates.append(value)
            sleep(self.interval)
        return value
