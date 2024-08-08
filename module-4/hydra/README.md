# Hydra

This folder contains the source code for my own implementation of the `hydra` tool.
Hydra can be used to attack hosts with SSH by forcing the password for a username.

This is a command-line tool that covers the following features:

-   Dictionary attack with a wordlist
-   Bruteforce attack with a defined characterset and password length

<br>

> [!CAUTION]
> Only attack your own local machines!

<br>

## Technologies

- Python 3.12.3
- Paramiko 3.4.0

## Getting started

1. Clone the repository:
```shell
git@github.com:mikemeyer186/dso-python-tasks.git
```

2. Create and activate virtual environment:
```shell
python -m venv <name of your environment>
source <name of your environment>/bin/activate
```

3. Change to directory `/hydra`:
```shell
cd module-4/hydra
```

4. Install dependencies:
```shell
python install -r requirements.txt
```

## Usage

Execute `hydra` in your command-line and show all available options:
```shell
python hydra.py -h
# or
python hydra.py --help
```

## Available options

| Option                  | Description                                                 | Required |
| ----------------------- | ----------------------------------------------------------- | -------- |
| `-u` <br> `--username`  | Username to login on sever with SSH                         |     x    |
| `-s` <br> `--server`    | DNS of server or IP address with or without port            |     x    |
| `-w` <br> `--wordlist`  | Wordlist for dictionary attack (e.g. "rockyou.txt")         |          |
| `-c` <br> `--character` | Charset for bruteforce attack   (default = "Aa1!")          |          |
| `--min` <br> `--minimum`| Minimum length of passwords for bruteforce (default = 4)    |          |
| `--max` <br> `--maximum`| Maximum length of passwords for bruteforce (default = 10)   |          |

<br>

> [!NOTE]
> Type a port behind the IP address like: `localhost:2222`
> <br>
> If you don't type a specific port, the default port is 80


## Examples

### Dictionary attack

Execute `hydra` with a dictionary attack:
```shell
python hydra.py \
-u <user> \
-s <DNS or IP address> \
-w <path to wordlist>
```

<br>

### Bruteforce attack

Execute `hydra` with a bruteforce attack (with default values):
```shell
python hydra.py \
-u <user> \
-s <DNS or IP address>
```

Execute `hydra` with a bruteforce attack with defined characters and password length:
```shell
python hydra.py \
-u <user> \
-s <DNS or IP address> \
-c Aa \
-min 4 \
-max 8    
```

> [!NOTE]
> Enter the characterset like this: `Aa1!`

<br>

Available characters:

| Option | Character          |
| ------ | -------------------|
| A      | Uppercase          |
| a      | Lowercase          |
| 1      | Numbers            |
| !      | Special Characters |

