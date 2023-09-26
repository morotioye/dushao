
import random as ra
import time as t
from git import Repo
import os

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

# chinese letters w/ tones (0-10) TODO add more nums, chat gpt can do it

ns = {
        0 : 'ling2',
        1 : 'yi1 - yao1',
        2 : 'er4',
        3 : 'san1',
        4 : 'si4',
        5 : 'wu3',
        6 : 'liu4',
        7 : 'qi1',
        8 : 'ba1',
        9 : 'jiu3',
        10 : 'shi2'
    }  

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
        f.write(f"{scst}\n")
    
    # Commit the changes
    repo.git.add(scores_file)
    repo.git.commit('-m', 'Add new score')
    
    # Push the changes
    origin.push()

def ses():
    m = 11
    while m > 10:
        m = int(input("what number should we go to? (max 10) : "))

    sm = 0
    sc = 0

    ord = req(m+1,m) 
    for n in ord:   
        print(f"{n} : ")
        st = t.time()  
        g = input("ans : ")
        if n == 1 and g == "yao1" or g == "yi1":
            sc += 1
        if g == ns[n]:
            sc += 1
        et = t.time() - st 
        sm += et
        print(ns[n])
        input("next : ")
    
    et -= m-sc
    score = sc * et
    print(round(sm, 3), " seconds.\n")
    print("score:", round(score, 3))

    tt = t.gmtime()
    ft = t.strftime("%Y-%m-%d %H:%M:%S", tt)

    with open("scores.txt", "w") as f:
        wr = f.write(f"max: {m}         score: {round(score, 3)}         log_time:{ft}\n")

    chc = input("submit score? (y/n) : ")
    if chc == "Y" or chc == "y":
        sbm(wr)
        print("score submitted.\n")
    
    chcc = input("again? (y/n) : ")
    if chcc == "Y" or chcc == "y":
        ses()
    else:
        print("bye.")



ses()
