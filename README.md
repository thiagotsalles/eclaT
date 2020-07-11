# eclaT

A function for ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal) algorithm.

  - *eclaT(text_file, min_grp=1, min_sup=1)*
  - text_file: txt file containing events, separated by line break, that contains a sequence (group) of items, separated by comma. Cannot contain events with repeated items.
  - min_grp: minimum group size to be shown in results.
  - min_sup: minimum support (group occurences) to be considered.


### Performance
Routine to test performance in *test.py*.

With *mysetup* containing the *eclaT* function definition plus:
```python
# File with a sequence of 100 events to test eclaT function
from random import randint, sample
event_items = ['item{}'.format(randint(1, 10)) for x in range(50)]
events = [set(sample(event_items, k=randint(1, 6))) for x in range(100)]
with open('events.txt', 'w') as f:
    for event in events:
        s = ', '.join(event)
        f.write('{}\\n'.format(s))

data = 'events.txt'
```
And *mycode* as:
```python
mycode = "eclaT(data, min_grp=2, min_sup=3)"
```
Time to execute 100, 1000 and 1000 loops with the txt file containing 100 events:
```python
import timeit
print(timeit.timeit(setup = mysetup, stmt = mycode, number = 100))
>>> 0.6727386000002298
print(timeit.timeit(setup = mysetup, stmt = mycode, number = 1000))
>>> 5.949157500000183
print(timeit.timeit(setup = mysetup, stmt = mycode, number = 1000))
>>> 81.58231419999993
```


