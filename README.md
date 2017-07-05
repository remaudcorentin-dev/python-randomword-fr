# python-randomword-fr

##### v1.0.0

Simple API python to get random words with definition (offline usage - French words & definitions)

### Installation

`pip install python-randomword-fr`


### Usage

```python

from randomwordfr import RandomWordFr

rw = RandomWordFr()

for i in range(0, 5):
    result = rw.get()
    print("# %s\n%s\n" % (result['word'], result['definition']))

```

or simply :

```python
>>> from randomwordfr import RandomWordFr
>>> print( RandomWordFr() )
# Cistre
Nom masculin.
Du latin « cithara » qui donna « citre » puis devint « cistre » par
confusion avec « sistre » (autre instrument de musique).
Instrument de musique à cordes pincées, analogue à la mandoline et qui
était en usage aux XVIème et XVIIème siècle.
```
