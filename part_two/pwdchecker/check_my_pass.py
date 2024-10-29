import requests
import hashlib
import sys

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError("failed fetching")
    return res

def read_res(response):
    pass

def get_leaked_pass_to_check(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        if h == hash_to_check:
            return c
    return 0

def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars, tail = sha1pass[:5], sha1pass[5:]
    res = request_api_data(first_5_chars)

    return get_leaked_pass_to_check(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times')
        else:
            print("good password")

if __name__ == '__main__':
    main(sys.argv[1:])

