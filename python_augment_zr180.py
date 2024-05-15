#pip install Augmentor

import Augmentor
import itertools
p = Augmentor.Pipeline(r"C:\Users\User\Desktop\augmented_final\zr180")
p.rotate180(probability=1)

n = 1
for _ in itertools.repeat(None, n):
    p.process()    # or p.sample(0) for that matter