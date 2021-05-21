import time
from gen_celery.gen_celery2 import celeryA
#from celery import Celery
from gevent import monkey
#from taskB import tB


monkey.patch_all()

# celeryA = Celery(backend='redis://localhost:6379/1',
#              broker='redis://localhost:6379/0')
#celeryA.config_from_object('celery_configA')

@celeryA.task()
def tA(i):
    time.sleep(5)
    with open('./A/'+str(i)+'.txt', 'w', encoding='utf-8') as f:
        f.write('A'+str(i))
