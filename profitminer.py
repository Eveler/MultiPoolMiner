# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import argparse
import json


class ProfitMiner:
    def __init__(self, args):
        self.__all_algorithms = self.load_algorithms("Algorithms.txt")
        algorithms = args.algorithm.lower().split(',')
        excluded_algorithms = self.__all_algorithms.keys() - algorithms
        self.__all_regions = self.load_regions('Regions.txt')
        regions = args.region.lower().split(',')
        excluded_regions = self.__all_regions.keys() - regions

    def load_algorithms(self, file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    def load_regions(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-wallet', type=str,
                        default='17yRzYS6ZZPHb4stH7eiYTsKp8qncNq2eg')
    parser.add_argument('-username', type=str, default='Eveler')
    parser.add_argument('-workername', type=str, default='profitminer')
    parser.add_argument('-region', type=str, default='eu')
    parser.add_argument('-currency', type=str, default='btc,usd,rub')
    parser.add_argument('-type', type=str, default='amd,nvidia,cpu')
    parser.add_argument(
        '-poolname', type=str,
        default='miningpoolhub,miningpoolhubcoins,zpool,nicehash')
    parser.add_argument(
        '-algorithm', type=str,
        default='cryptonight,decred,decrednicehash,ethash,ethash2gb,equihash,'
                'groestl,lbry,lyra2z,neoscrypt,pascal,sia,siaclaymore,'
                'sianicehash,sib,bitcore,blake,blake2s,blakecoin,blakevanilla,'
                'c11,daggerhashimoto,darkcoinmod,eth,groestlcoin,hmq1725,jha,'
                'keccak,lyra2re2,lyra2rev2,lyra2v2,maxcoin,myrgr,'
                'myriadcoingroestl,myriadgroestl,nist5,quark,quarkcoin,qubit,'
                'qubitcoin,scrypt,sha256,sibcoinmod,sigt,skein,skeincoin,skunk,'
                'timetravel,tribus,vanilla,veltor,x11,x11gost,x11evo,x17,xevan,'
                'xmr,yescrypt,zec,zuikkis')
    parser.add_argument('-delay', type=int, default=0)
    parser.add_argument('-donate', type=int, default=10)
    args = parser.parse_args()

    pm = ProfitMiner(args)

    donate_wallet = '17yRzYS6ZZPHb4stH7eiYTsKp8qncNq2eg'
    donate_user = 'Eveler'
    donate_percent = args.donate if args.donate > 10 else 10
    donate_threshold = 100 - donate_percent


if __name__ == '__main__':
    # main()
    from core.plugin import load_plugins
    print(load_plugins('APIs'))
