
from randomwordfr import RandomWordFr

rw = RandomWordFr()

for i in range(0, 5):
    result = rw.get()
    print("# %s\n%s\n" % (result['word'], result['definition']))
