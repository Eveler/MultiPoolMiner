# -*- encoding: utf-8 -*-

# Author: Savenko Mike
from time import sleep

from core import Plugin


class Ccminer(Plugin):
    _name = "Ccminer"
    server = "localhost"
    timeout = 10  # seconds
    delta = 0.05
    interval = 5

    def get_hash_rate(self, algo, safe=False):
        hashrates = {}
        for a in algo:
            hr = []
            while len(hashrates) < 6:
                data = self.get_response_text()
                data = data.split(';')
                name = self.get_algorithm(data[a])
                value = data['KHS'] * 1000
                hr.append({name: value})
                if not safe:
                    break
                sleep(self.interval)

        return {'Average': sum(hashrates) / len(hashrates),
                'Maximum': max(hashrates), 'Minimum': min(hashrates),
                'Count': len(hashrates)}
