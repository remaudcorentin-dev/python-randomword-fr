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
