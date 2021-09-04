import sys

n_found = False
n = 0

people = list()

preferences = []

for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('#'):
        continue

    if not n_found:
        n = int(line.lstrip('n='))
        n_found = True
        preferences = [None] * (2*n)
        preferences_inv = [None] * (2*n)

        continue

    if len(people) < 2*n:
        people.append(line.split(' ', 1)[1])
        continue

    if line == '':
        continue

    split_line = line.split(': ', 1)
        
    preferences[int(split_line[0]) - 1] = list(list(map(lambda x: int(x) -
                                                                1, split_line[1].split(' '))))




# Create matrix containing men and women preferences respectively
#men_pref = ["man"]["ith woman on his preference"]
men_pref = []
for i in range(0, len(preferences), 2):
    men_pref.append(preferences[i])

women_pref = []
for i in range(1, len(preferences), 2):
    women_pref.append(preferences[i])

# Rescale them starting from 0.
# This will help with the algorithm.
for i in range(len(men_pref)):
    men_pref[i] = [int((x + 0) / 2) for x in men_pref[i]]
    women_pref[i] = [int(x / 2) for x in women_pref[i]]



# # Used for keeping track of the index of each person
proposers = list()
# rejectors = list()
# matches = [None] * (n*2)

for i in range(n*2):
    if i % 2 == 0:
        proposers.append(i)
#     else:
#         rejectors.append(i)



# PART 1 FROM BOOK

# Using dequeue as linked list 
from collections import deque

free_men = deque()
for man in range(len(proposers)):
    free_men.append(man)




# PART 2 OF BOOK

# List containing every man's next woman to propose to
_next = [0] * len(proposers)

def get_propose():
    man = free_men[0]
    woman = men_pref[man][_next[man]]
    _next[man] += 1
    return man, woman



# PART 3 OF BOOK

_current = ["-"] * len(proposers)



# PART 4 OF BOOK

_ranking = women_pref     #ranking[woman][rank of each man for that woman]
# for woman in range(len(women_pref)):
#     _ranking.append(women_pref[woman])

# w: woman, m: current man, m_i: proposing man
# Returns True if the matching is to be done
# i.e. if woman is single or proposing partner is better
def is_match(w, m, m_i):
    print(m_i)
    print(w)
    print(m)
    print("_________")
    if m == "-":
        return True
    if  _ranking[w].index(m_i) < _ranking[w].index(m):
        print(_ranking)
        print(_ranking[w][m_i])
        print(_ranking[w][m])
        return True


# Perform the algorithm.
# Check if it's a match (wither single woman or proposer is higher priority):
# if it is, remove the man from the free_men list,
# update the woman's current man, and if the woman was engaged with someone,
# put the "ex" in the free_men list again.
# Execute until there are no more free men.
while len(free_men) > 0:
    man, woman = get_propose()
    # print(man, woman)
    current_man = _current[woman]
    
    if is_match(woman, current_man, man):
        free_men.popleft()
        _current[woman] = man
        if current_man != "-":
            print("yes swap")
            free_men.appendleft(current_man)
            # print(free_men)
        
    


print(_current)


# print(preferences)
# print()
# print(proposers)
# print(men_pref)
# print(women_pref)
# print(free_men)

# print()
# print(_next)
# print(women_pref)
# print(_ranking)

