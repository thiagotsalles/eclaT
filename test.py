# -*- coding: utf-8 -*-

# Code snippet to be executed only once 
mysetup = """
# Importing packages
import pandas as pd
from collections import Counter
import itertools as it

def eclaT(text_file, min_grp=1, min_sup=1):
    # > text_file cannot contain events with repeated items.
    # > Event items must be separated by a comma.
    # > min_grp = Minimum group size
    # > min_sup = Minimal support
    
    if (min_grp < 1) or (min_sup < 1):
        print('Error: min_grp and min_sup should be > 1')
        return

    # Data frame with events
    with open(text_file) as f:
        num_cols = max(len(line.split(',')) for line in f) # Max cols
        f.seek(0)  # Resets the f reading cursor
        df = pd.read_csv(f, names=range(num_cols)); del num_cols
    
    list_1 = [  # List with events as sublists
              [str(x) for x in sublist if str(x) != 'nan']
              for sublist in df.values
             ]
    list_1 = [sorted(x) for x in list_1] # Sorts elements from sublists
    
    list_2 = [  # Possible groups (> 1) of the items for each event
              [comb for L in range(0, len(sublist) + 1)
              for comb in it.combinations(sublist, L)
              if len(comb) >= min_grp]
              for sublist in list_1
             ]
    list_2 = [x for x in list_2 if len(x) > 0] # Removes empty sublists
    
    l2_col = [x for sublist in list_2 for x in sublist] # Collapse of list_2
    conta = Counter(l2_col)  # Counts the occurrence of possible groups
    
    if min_sup > 1:
        eclat = [  # Groups, counts and occurrence (events)
                 [k, v, [i for i, sublist in enumerate(list_2, 1)
                 if k in sublist]]
                 for k, v in conta.items() if v >= min_sup
                ]
    else:
        eclat = [  # Groups, counts and occurrence (events)
                 [k, v, [i for i, sublist in enumerate(list_2, 1)
                 if k in sublist]]
                 for k, v in conta.items()
                ]
            
    col_nomes = ['Group', 'Support', 'Event']
    eclat_list = [  # List containing dictionaries with ECLAT results
                  {k: v for k, v in zip(col_nomes, sublist)}
                  for sublist in eclat
                 ]

    # Data frame with eclat_list
    eclat_df = pd.DataFrame.from_dict(eclat_list).reindex(col_nomes, axis=1)
    return eclat_df


# File with a sequence of 100 events to test eclaT function
from random import randint, sample
event_items = ['item{}'.format(randint(1, 10)) for x in range(50)]
events = [set(sample(event_items, k=randint(1, 6))) for x in range(100)]
with open('events.txt', 'w') as f:
    for event in events:
        s = ', '.join(event)
        f.write('{}\\n'.format(s))

data = 'events.txt'
"""


# Code snippet whose execution time is to be measured 
mycode = "eclaT(data, min_grp=2, min_sup=3)"

# Timeit statement
import timeit
print(timeit.timeit(setup = mysetup, 
                    stmt = mycode, 
                    number = 100))

print(timeit.timeit(setup = mysetup, 
                    stmt = mycode, 
                    number = 1000))

print(timeit.timeit(setup = mysetup, 
                    stmt = mycode, 
                    number = 1000))


