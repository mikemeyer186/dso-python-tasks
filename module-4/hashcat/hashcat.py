from itertools import product
from argparse import ArgumentParser
from hashlib import sha1, sha256, sha512, md5
import string

parser = ArgumentParser(description='Educational version of Hashcat')

parser.add_argument('-m', '--mode', type=int, help='Hashmode: 0=MD5, 1=SHA-1, 2=SHA-256, 3=SHA-512', required=True)
parser.add_argument('-a', '--attack', type=int, help='Attackmode: 0=Brute-Force Attack, 1=Dictionary Attack', required=True)
parser.add_argument('-s', '--hash', type=str, help='Hash')
parser.add_argument('-S', '--hashfile', type=str, help='Path and filename of a hashfile')
parser.add_argument('-W', '--wordlist', type=str, help='Path and filename of a wordlist')
parser.add_argument('-min', '--minimum', default=4, type=int, help='Minimum length of password')
parser.add_argument('-max', '--maximum', default=12, type=int, help='Maximum length of password')

args = parser.parse_args()

attackmode = args.attack
hashmode = args.mode
hashfile = args.hashfile
wordlist = args.wordlist
charSet = string.ascii_letters + string.digits + string.punctuation

def calculate_hash_md5(pwd: str) -> str:
    """
    Calculates the hash value of pwd parameter
    with hashalgorithm MD5.

    Parameters:
    pwd (str): Password of bruteforce or dictionary attack

    Returns:
    str: Hash value in hex view
    """
    md5_hash = md5(pwd.encode())
    hex = md5_hash.hexdigest()
    return hex

def calculate_hash_sha1(pwd: str) -> str:
    """
    Calculates the hash value of pwd parameter
    with hashalgorithm SHA-1.

    Parameters:
    pwd (str): Password of bruteforce or dictionary attack

    Returns:
    str: Hash value in hex view
    """
    sha1_hash = sha1(pwd.encode())
    hex = sha1_hash.hexdigest()
    return hex

def calculate_hash_sha256(pwd: str) -> str:
    """
    Calculates the hash value of pwd parameter
    with hashalgorithm SHA-256.

    Parameters:
    pwd (str): Password of bruteforce or dictionary attack

    Returns:
    str: Hash value in hex view
    """
    sha256_hash = sha256(pwd.encode())
    hex = sha256_hash.hexdigest()
    return hex

def calculate_hash_sha512(pwd: str) -> str:
    """
    Calculates the hash value of pwd parameter 
    with hashalgorithm SHA-512.

    Parameters:
    pwd (str): Password of bruteforce or dictionary attack

    Returns:
    str: Hash value in hex view
    """
    sha512_hash = sha512(pwd.encode())
    hex = sha512_hash.hexdigest()
    return hex

def check_hashfile() -> str:
    """
    Checks if a hashfile is prompted by user and returns the hash value (file or command)

    Returns:
    str: Hash value in hex view
    """
    hash = args.hash

    if hashfile:
        with open(hashfile, 'r', encoding='utf-8') as file:
            hash = file.read().strip()

    return hash

def choose_hashmode(pwd: str):
    """
    Checks which hashmode is choosen by user and calculates the hashvalue 
    with the corresponding function.
    
    Parameters:
    pwd (str): Password of bruteforce or dictionary attack
    """
    try:
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
                raise ValueError("Invalid hashmode! Please select 0 for MD5, 1 for SHA-1, 2 for SHA256 or 3 for SHA512")   
    except ValueError as e:
            print(f"ValueError: {e}.")
            exit()

def compare_hash_and_password(hash: str, pwd_hash: str, pwd: str, number: int):
    """
    Compares the calculated hashvalue and the hashvalue from user input.
    
    Parameters:
    hash (str): Hash vlue from command or from hashfile
    pwd_hash (str): Password hash of bruteforce or dictionary attack
    pwd (str): Password of bruteforce or dictionary attack
    number (int): Number of attempts (password or combinations)
    """
    if pwd_hash == hash:
        print(f'CRACKED! {number} passwords checked -> the password is \'{pwd}\'!')
        exit()

def dictionary_attack(hash: str):
    """
    Reads single passwords of the wordlist, calculates the hash value 
    and compares with hashvalue from user input.

    Parameters:
    hash (str): Hash vlue from command or from hashfile
    """
    with open(wordlist, 'r') as list:
        number = 0
        for password in list.readlines():
            number += 1
            pwd = password.strip()
            pwd_hash = choose_hashmode(pwd)
            compare_hash_and_password(hash, pwd_hash, pwd, number)
        print(f'{number} passwords checked. Password not found. Please try another wordlist.')
      
def bruteforce_attack(hash: str):
    """
    Executes the brutforce attack with default characterset (Aa1!), entered length of password (default 4 - 12), 
    calculates the hash value and compares with hashvalue from user input.

    Parameters:
    hash (str): Hash vlue from command or from hashfile
    """
    for n in range (args.minimum, args.maximum + 1):
        number = 0
        for password in product(charSet, repeat=n):
            number += 1
            pwd = "".join(password)
            pwd_hash = choose_hashmode(pwd)
            compare_hash_and_password(hash, pwd_hash, pwd, number)
    print(f'{number} password not found. Please adjust the min and max length.')

if __name__ == "__main__":
    hash = check_hashfile()

    try:
        if attackmode == 0:
            bruteforce_attack(hash)
        elif attackmode == 1:
            dictionary_attack(hash)
        else:
            raise ValueError("Invalid attackmode! Please select 0 for bruteforce or 1 for dictionary attack")
    except ValueError as e:
        print(f"ValueError: {e}.")
        exit()