# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:33:28 2019

A function for ECLAT (Equivalence Class Clustering and bottom-up Lattice
Traversal) algorithm.
"""

# Importing packages
import pandas as pd
from collections import Counter
import itertools as it

def eclaT(text_file, min_grp=1, min_sup=1):
    # text_file: txt file containing events, separated by line break, that
    # contains a sequence (group) of items, separated by comma. Cannot contain
    # events with repeated items.
    # min_grp: minimum group size to be shown in results.
    # min_sup: minimum support (group occurences) to be considered.
    
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
            
    col_nomes = ['Group', 'Support', "Event']
    eclat_list = [  # List containing dictionaries with ECLAT results
                  {k: v for k, v in zip(col_nomes, sublist)}
                  for sublist in eclat
                 ]

    # Data frame with eclat_list
    eclat_df = pd.DataFrame.from_dict(eclat_list).reindex(col_nomes, axis=1)
    return eclat_df


