# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import logging

from requests import request

from core import Plugin


class NiceHash(Plugin):
    def __init__(self, callback=None):
        super().__init__()
        self.name = self._get_class_name()
        self.__get_algo = callback
        self.regions = ("eu", "usa", "hk", "jp", "in", "br")

    def stats(self, callback=None):
        get_algo = callback if callback else self.__get_algo
        try:
            req = request(
                'GET',
                "http://api.nicehash.com/api?method=simplemultialgo.info")
            res = req.json()['result']['simplemultialgo']
            if not res:
                logging.warning("Pool API (%s) returned nothing." % self.name)
            st = {}
            for item in res:
                name = item['name']
                if get_algo:
                    name = get_algo(name)
                if name == "Sia":
                    name = "SiaNiceHash"
                if name == "Decred":
                    name = "DecredNiceHash"
                divisor = 1000000000
                st[name] = {'host': "nicehash.com", 'port': item['port'],
                            'algorithm': item['name'],
                            'stat': {
                                'name': item['name'] + "_" + name + "_Profit",
                                'value': float(item['paying']) / divisor,
                                'duration': 'day'}}
            return st
        except:
            logging.warning("Pool API (%s) has failed." % self.name)
            logging.debug("", exc_info=True)
            return {}


if __name__ == '__main__':
    logging.root.setLevel(logging.DEBUG)
    nh = NiceHash()
    print(nh.stats())
