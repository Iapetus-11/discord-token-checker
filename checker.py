"""Made by Iapetus-11"""

import multiprocessing as mp
import requests as rs

def check(t): return t if rs.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': t}).status_code == 200 else 'None'

if __name__ == '__main__':
    with mp.Pool(20) as p:
        with open('tokens.txt', 'r') as f:
            split = f.read().strip('\n').split('\n')
            working = (*filter((lambda t: t != 'None'), set(p.map(check, split))),)

            with open('working.txt', 'w+') as f2:
                f2.write('\n'.join(working))

            print(f'Working (actual tokens in working.txt): {len(working)}/{len(split)}')
