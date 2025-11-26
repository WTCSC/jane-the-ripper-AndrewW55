import hashlib
import csv

hashes = set()
wordlist = []

def hashOpener(path):
    try:
        with open(path) as file:
            for line in file:
                hashes.add(line.strip())
    except FileNotFoundError:
        print("Error with opening hash file, please try again")

def wordHash(path):
    try:
        with open(path) as file:
            for line in file:
                og_line = line.strip()
                hash = hashlib.md5()
                hash.update(og_line.encode('utf-8'))
                hash = hash.hexdigest()
                if hash in hashes:
                    print(f"CRACKED[{hash}]")
                else:
                    print(f"UNCRACKED[{hash}]")

    except FileNotFoundError:
        print("Error finding wordlist file, please try again")

def main():
    hashpath = input("What is the name to your hash file? ")
    wordpath = input("What is the name of your wordlist file? ")

    hashOpener(hashpath)
    wordHash(wordpath)

main()