from itertools import product
from argparse import ArgumentParser
import hashlib
import string

parser = ArgumentParser(description='Educational version of Hashcat')

parser.add_argument('-m', '--mode', type=int, help='Hashmode: 0=MD5, 1=SHA-1, 2=SHA-256, 3=SHA-512', required='True')
parser.add_argument('-a', '--attack', type=int, help='Attackmode: 0=Brute-Force Attack, 1=Dictionary Attack', required='True')
parser.add_argument('-s', '--hash', type=str, help='Hash')
parser.add_argument('-S', '--hashfile', type=str, help='Path and filename of a hasfile')
parser.add_argument('-W', '--wordlist', type=str, help='Path and filename of a wordlist')

args = parser.parse_args()

attackmode = args.attack
hashmode = args.mode
hash = args.hash
hashfile = args.hashfile
wordlist = args.wordlist
charSet = string.ascii_letters + string.digits + string.punctuation

def calculate_hash_md5(pwd: str) -> str:
    md5_hash = hashlib.md5(pwd.encode())
    hex = md5_hash.hexdigest()
    return hex

def calculate_hash_sha1(pwd: str) -> str:
    sha1_hash = hashlib.sha1(pwd.encode())
    hex = sha1_hash.hexdigest()
    return hex

def calculate_hash_sha256(pwd: str) -> str:
    sha256_hash = hashlib.sha256(pwd.encode())
    hex = sha256_hash.hexdigest()
    return hex

def calculate_hash_sha512(pwd: str) -> str:
    sha512_hash = hashlib.sha512(pwd.encode())
    hex = sha512_hash.hexdigest()
    return hex

def check_hashmode(pwd: str):
    match hashmode:
        case 0:
           return calculate_hash_md5(pwd) 
        case 1:
           return calculate_hash_sha1(pwd) 
        case 2:
           return calculate_hash_sha256(pwd) 
        case 3:
           return calculate_hash_sha512(pwd) 
        case _:
            print("Please enter a valid hashmode!")
            exit()

def compare_hash_and_password(pwd_hash, pwd):
    if pwd_hash == hash:
        print(f'The password is \'{pwd}\'!')
        exit()

def dictionary_attack():
    """
    Reads single passwords of the wordlist and tries to connect.
    """
    with open(wordlist, 'r') as list:
        for password in list.readlines():
            pwd = password.strip()
            pwd_hash = check_hashmode(pwd)
            compare_hash_and_password(pwd_hash, pwd)
        print(f'Password not found. Please try another wordlist.')
      
def bruteforce_attack():
    """
    Executes the brutforce attack with characterset and length of password 
    defined by user and tries to connect.
    """
    for n in range (6, 7):
        for password in product(charSet, repeat=n):
            pwd = "".join(password)
            pwd_hash = check_hashmode(pwd)
            compare_hash_and_password(pwd_hash, pwd)
    print(f'Password not found. Please adjust the characters and the min and max length.')

if __name__ == "__main__":
    if attackmode == 0:
        bruteforce_attack()
    else:
        dictionary_attack()