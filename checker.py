import multiprocessing as mp
import requests as rs

check = (lambda t: rs.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': t}).status_code == 200)

if __name__ == '__main__':
    with mp.Pool(20) as p:
        with open('tokens.txt', 'r') as f:
            print(p.map(check, f.readlines()))
