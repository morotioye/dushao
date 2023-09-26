import random as ra

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

def ses():
    m = 11
    while m > 10:
        m = int(input("what number should we go to? (max 10) : "))

    ord = req(m+1,m) # have the sequence of nums
    for n in ord:   
        print(f"{n} : ")
        input("enter : ")
        print(ns[n])
        input("enter : ")

# TODO add 'easy' 'hard' 'fail'

ses()

# enter max 
# show number
# user returns anything
# return letter
# user returns anything
# show next number