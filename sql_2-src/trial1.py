from hashlib import sha256
import re
import random

def match(text):
    rule = re.compile("' [Oo][Rr]")
    rule = re.compile("'[Oo][Rr]'[123456789]")
    result = re.findall(rule, text)
    if len(result) > 0:
        return True
    return False    

def main():
    for i in range(10000000000):
        c = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQAZWSXEDCRFVTGBYHNUJMIKOLP'
        guess = ''
        for j in range(256):
            guess += (random.choice(c))
        # guess = str(int(random.random() * (1<<128)))
        password = ("bungle-" + guess).encode("latin-1")

        digest = sha256(password).digest().decode("latin-1")
        # if i % 100000 == 0:
        #     print(guess)
        #     print(digest)
        
        if match(digest):
            print(guess)
            print(digest)
            print("MATCH!!!!!!!!!!!!")
            return 
main()