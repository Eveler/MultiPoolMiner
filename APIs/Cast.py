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
            data = self.get_response_json()
            value = sum(data['devices']['hash_rate']) / 1000
            hashrates.append(value)
            if not safe:
                break
            value = sum(data['devices']['hash_rate_avg']) / 1000
            if value:
                hashrates.append(value)
            sleep(self.interval)
        return {algo[0]: {'Average': sum(hashrates) / len(hashrates),
                          'Maximum': max(hashrates), 'Minimum': min(hashrates),
                          'Count': len(hashrates)}}
