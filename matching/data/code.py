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

    preferences[int(split_line[0]) - 1] = list(reversed(list(map(lambda x: int(x) -
                                                                1, split_line[1].split(' ')))))

# Insert int indicating the number of the man/woman whose preference list belongs to.
# There is no risk of confusion because a man will be an even number in a list of odd numbers
# and vice-versa, and they will always be in position 0 anyways.
# Inserted as int rather than list for accesibility purposes.
for i in range(len(preferences)):
    preferences[i].insert(0,i)


# Create matrix containing men and women preferences respectively
men_pref = []
for i in range(0, len(preferences), 2):
    men_pref.append(preferences[i])

women_pref = []
for i in range(1, len(preferences), 2):
    women_pref.append(preferences[i])


# Used for keeping track of the index of each person
proposers = list()
rejectors = list()
matches = [None] * (n*2)

for i in range(n*2):
    if i % 2 == 0:
        proposers.append(i)
    else:
        rejectors.append(i)


# Using dequeue as linked list 
from collections import deque

free_men = deque()
for man in proposers:
    free_men.append(man)



# List containing every man's next woman to propose to
_next = [0] * len(proposers)

# List containing every woman's current partner
_current = ["-"] * len(rejectors)



# Returns man and respective woman for next proposal round.
# For the man: takes the first man from the linked list.
# For the woman: finds the sub-list of the respective man,
# then uses the "_next" list to see which woman to propose next,
# and finds the number of that woman.
# The man's counter for which woman to proposed next is finally increased. 
def get_man_and_woman():
    man = free_men[0]
    for i in range(len(men_pref)):
        if man in men_pref[i]:
            woman = men_pref[i][_next[proposers.index(man)] + 1]
    _next[proposers.index(man)] += 1
    return man, woman



def propose():
    _ranking = [[]]
    for woman in women_pref:
        return 


print(preferences)
print()
print(proposers)
print(men_pref)
print(free_men)

print()
print(_next)
print(women_pref)










# def is_better_match(proposed_to, proposer):
#     return preferences[proposed_to].index(proposer) > preferences[proposed_to].index(matches[proposed_to])


# while len(proposers) > 0:
#     proposer = proposers.pop()

#     preference = preferences[proposer].pop()

#     if matches[preference] is None:
#         matches[preference] = proposer
#         matches[proposer] = preference

#     elif is_better_match(preference, proposer):
#         matches[matches[preference]] = None
#         proposers.append(matches[preference])

#         matches[proposer] = preference
#         matches[preference] = proposer
#     else:
#         proposers.append(proposer)

# for i in range(len(people)):
#     if (i % 2 == 0):
#         print(people[i] + ' -- ' + people[matches[i]])