# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import logging
from time import sleep

from core import Plugin


class Ccminer(Plugin):
    _name = "Ccminer"
    server = "localhost"
    timeout = 10  # seconds
    delta = 0.05
    interval = 5

    def get_hash_rate(self, algo, safe=False):
        def measure(v):
            if max(v) - min(v) >= self.delta * sum(v) / len(v):
                return {'Average': sum(v) / len(v), 'Maximum': max(v),
                        'Minimum': min(v), 'Count': len(v)}
            else:
                return {'Average': 0, 'Maximum': 0, 'Minimum': 0, 'Count': 0}

        hashrates = {}
        for a in algo:
            while len(hashrates) < 6:
                data = self.get_response_text()
                data = data.split(';')
                logging.debug(data)
                name = self.get_algorithm(data[a])
                hashrates[name] = []
                value = data['KHS'] * 1000
                hashrates[name].append(value)
                if not safe:
                    break
                sleep(self.interval)
            hashrates = {k: measure(v) for k, v in hashrates.items()}

        return hashrates
