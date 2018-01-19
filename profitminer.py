# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import argparse
import json


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
    args = parser.parse_args('-algorithm cryptonight,decred'.split())

    with open("Algorithms.txt", "r") as f:
        all_algorithms = json.load(f)
    algorithms = args.algorithm.lower().split(',')
    excluded_algorithms = all_algorithms.keys() - algorithms

    with open('Regions.txt', 'r') as f:
        all_regions = json.load(f)

    donate_wallet = '17yRzYS6ZZPHb4stH7eiYTsKp8qncNq2eg'
    donate_user = 'Eveler'


if __name__ == '__main__':
    main()
