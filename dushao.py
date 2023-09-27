import json
import random as ra
import time as t
from git import Repo
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\03……3[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# method to get n distinct nums between 0 and m (both included)
def req(n, m):
    if n == 0 or m == 0 or n > m + 1:
        return []
    
    r = []
    while len(r) < n:
        nm = ra.randint(0, m)
        while nm in r:
            nm = ra.randint(0,m)
        r.append(nm)
        
    return list(r)

def sbm(scst):
    # Clone the repository
    repo_dir = "/Users/wnr/bai/dushao/"

    repo_url = "https://github.com/seeohh/dushao.git"
    if not os.path.exists(repo_dir):
        repo = Repo.clone_from(repo_url, repo_dir)
    else:
        repo = Repo(repo_dir)
    
    # Pull the latest changes
    origin = repo.remotes.origin
    origin.pull()
    
    # Append the new score to scores.txt
    scores_file = os.path.join(repo_dir, "scores.txt")
    with open(scores_file, "a") as f:
        f.write(f"{scst}\n\n")
    
    # Commit the changes
    repo.git.add(scores_file)
    repo.git.commit('-m', 'Add new score')
    
    # Push the changes
    origin.push()

def nses():
    with open("nums.json", "r") as f:
        ns = json.load(f)

    m = 11
    while m > 10:
        m = int(input("what number should we go to? (max 10) : "))

    sm = 0
    sc = 0

    input("set your keyboard to chinese. - enter on ready : ")
    ord = req(m+1,m) 
    for idx, n in enumerate(ord, start=1):   
        print(f"{Colors.OKCYAN}Question {idx}/{len(ord)}: {n}{Colors.ENDC}")
        st = t.time()  
        g = input("ans : ")
        if n == 1 and (g == "一" or g == "幺"):
            print(f"{Colors.OKGREEN}hit{Colors.ENDC}")
            sc += 1
        elif g == ns[str(n)]:
            sc += 1
            print(f"{Colors.OKGREEN}hit{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}miss{Colors.ENDC}")
        et = t.time() - st 
        sm += et
        print(ns[str(n)])
    
    sm -= m-sc
    score = sc * sm
    print(round(sm, 3), " seconds.\n")
    print("score:", round(score, 3))

    tt = t.gmtime()
    ft = t.strftime("%Y-%m-%d %H:%M:%S", tt)

    with open("scores.txt", "a") as f:
        wr = f.write(f"max: {m}         score: {round(score, 3)}         log_time:{ft}")

    chc = input("submit score? (y/n) : ")
    if chc == "Y" or chc == "y":
        sbm(wr)
        print("score submitted.\n")
    
    chcc = input("again? (y/n) : ")
    if chcc == "Y" or chcc == "y":
        dushao()
    else:
        print("bye.")

def cses():
    with open("chars.json", "r") as f:
        cs = json.load(f)

    with open("pinyin.json", "r") as pf:
        ps = json.load(pf)

    cts = int(input("how many characters would you like to practice? (max 61): "))
    if cts > len(cs) or cts <= 0:
        print("Invalid number of characters.")
        return

    # Select random keys from the dictionary
    selected_keys = ra.sample(list(cs.keys()), cts)
    sc = 0
    sm = 0

    input("set your keyboard to chinese. - enter on ready : ")
    selected_keys = ra.sample(list(cs.keys()), cts)
    for idx, key in enumerate(selected_keys, start=1):
        print(f"{Colors.OKCYAN}Question {idx}/{len(selected_keys)}: {key}{Colors.ENDC}")
        stt = t.time()
        g = input("ans : ")
        if g == cs[key]:
            print(f"{Colors.OKGREEN}hit{Colors.ENDC}")
            sc += 1
        else:
            print(f"{Colors.FAIL}miss{Colors.ENDC}")
        et = t.time() - stt
        sm += et
        print(cs[key], ps[key])

    sm -= cts - sc
    score = sc * sm
    print(round(sm, 3), " seconds.\n")
    print("score:", round(score, 3))

    tt = t.gmtime()
    ft = t.strftime("%Y-%m-%d %H:%M:%S", tt)

    with open("scores.txt", "a") as f:
        wr = f.write(f"max: {cts}         score: {round(score, 3)}         log_time:{ft}")

    chc = input("submit score? (y/n) : ")
    if chc.lower() == "y":
        sbm(wr)
        print("score submitted.\n")

    chcc = input("again? (y/n) : ")
    if chcc.lower() == "y":
        dushao()
    else:
        print("bye.")



def dushao():
    print(Colors.HEADER + "Welcome to DuShao!" + Colors.ENDC)
    c = input("please select an option: \n" + Colors.OKCYAN + "numbers (1)\nwords (2)\n" + Colors.ENDC + ": ")
    if c == "1":
        nses()
    elif c == "2": 
        cses()
    else:
        dushao()


dushao()