# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import json

from .plugin import load_plugins

DONATE_PERCENT = 5


class ProfitMiner:
    def __init__(self, args):
        self.__all_algorithms = self.load_algorithms("Algorithms.txt")
        self.algorithms = args.algorithm.lower().split(',')
        self.excluded_algorithms = self.__all_algorithms.keys() - self.algorithms
        if not self.algorithms:
            self.algorithms = self.__all_algorithms
            self.excluded_algorithms = []
        self.__all_regions = self.load_regions('Regions.txt')
        self.regions = args.region.lower().split(',')
        self.excluded_regions = self.__all_regions.keys() - self.regions
        self.apis = self.load_apis()
        self.instances = []
        self.donate_wallet = '17yRzYS6ZZPHb4stH7eiYTsKp8qncNq2eg'
        self.donate_user = 'Eveler'
        self.donate_percent = args.donate if args.donate > DONATE_PERCENT else DONATE_PERCENT
        self.donate_threshold = 100 - self.donate_percent

    def step(self):
        """
        Update profits from mining instances.
        If no mining instances load profits from files.
        Sort profits.
        Start most profitable algorithm by appropriate miner on best pool for each selected device.
        """
        for i in self.instances:
            i.stats()

        self.donate_threshold -= 1
        if self.donate_threshold:
            self.donate_threshold = 100 - self.donate_percent

    def load_algorithms(self, file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    def load_regions(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    def load_apis(self, dir_path='APIs'):
        # for plugin in load_plugins(dir_path):
        #     print(plugin, ":", plugin.get_response(
        #         'http://api.nicehash.com/api?method=simplemultialgo.info'))
        return load_plugins(dir_path)

    def load_pools(self, dir_path='Pools'):
        return load_plugins(dir_path, self.get_algorithm)

    def get_algorithm(self, algo):
        algo = algo.replace('-', '').replace('_', '').replace(' ', '').lower()
        algo = algo[0].upper() + algo[1:]
        return self.__all_algorithms[
            algo] if algo in self.__all_algorithms else algo
