# Hashcat

This folder contains the source code for my own implementation of the `hashcat` tool.
Hashcat can be used to compare entered hashvalues with calculated hashvalues from a dictionary or a bruteforce attack.

This is a command-line tool that covers the following features:

-   Calculating hash values with 4 different algorithms
-   Dictionary attack with a wordlist
-   Bruteforce attack with a default characterset and individual password length

<br>

> [!CAUTION]
> Only crack your own passwords!

<br>

## Technologies

-   Python 3.12.3
-   hashlib (core library)

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

3. Change to directory `/hashcat`:

```shell
cd module-4/hashcat
```

4. Install dependencies:

```shell
python install -r requirements.txt
```

## Usage

Execute `hashcat` in your command-line and show all available options:

```shell
python hashcat.py -h
# or
python hashcat.py --help
```

## Available options

| Option                  | Description                                           | Required |
| ----------------------- | ----------------------------------------------------- | -------- |
| `-m` <br> `--mode`      | Hashmode: 0=MD5, 1=SHA-1, 2=SHA-256, 3=SHA-512        | x        |
| `-a` <br> `--attack`    | Attackmode: 0=Brute-Force Attack, 1=Dictionary Attack | x        |
| `-s` <br> `--hash`      | Hash value                                            |          |
| `-S` <br> `--hashfile`  | Path and filename of a hashfile (e.g. txt-file)       |          |
| `-W` <br> `--wordlist`  | Path and filename of a wordlist (e.g. "rockyou.txt")  |          |
| `-min` <br> `--minimum` | Minimum length of password                            |          |
| `-max` <br> `--maximum` | Maximum length of password                            |          |

<br>

> [!NOTE]
> For bruteforce attack a default characterset will be used (Aa1!) and a default length of the password will be used (range 4 - 10 characters)

<br>

## Examples

### Dictionary attack

Execute `hashcat` with a dictionary attack, hashalgorithm SHA-512 and a hash value in a file:

```shell
python hashcat.py \
  -m 3 \
  -a 1 \
  -W <path to wordlist> \
  -S <path to hashfile>
```

<br>

Execute `hashcat` with a dictionary attack, hashalgorithm SHA-1 and a hash value in the command:

```shell
python hashcat.py \
  -m 1 \
  -a 1 \
  -W <path to wordlist> \
  -s <your hash value>
```

<br>

### Bruteforce attack

Execute `hashcat` with a bruteforce attack, hashalgorithm SHA-256 and a hash value in the command:

```shell
python hashcat.py \
  -m 2 \
  -a 0 \
  -s <your hash value> \
  -min 6
```

<br>

Execute `hashcat` with a bruteforce attack, hashalgorithm MD5 and a hash value in a file:

```shell
python hashcat.py \
  -m 0 \
  -a 0 \
  -S <path to hashfile> \
  -min 8 \
  -max 12
```
