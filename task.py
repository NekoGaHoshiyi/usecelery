from taskA import tA
from taskB import tB


for i in range(600):
        tA.apply_async((i,))
        tB.apply_async((i,))