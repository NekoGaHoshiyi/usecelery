import time
from gen_celery.gen_celery2 import celeryB
#from celery import Celery
from gevent import monkey

monkey.patch_all()

# celeryA = Celery(backend='redis://localhost:6379/1',
#              broker='redis://localhost:6379/0')
#celeryA.config_from_object('celery_configA')

@celeryB.task()
def tB(i):
    time.sleep(5)
    with open('./B/'+str(i)+'.txt', 'w', encoding='utf-8') as f:
        f.write('B'+str(i))

# 由此可见，不要随便在代码内留多余的函数调用，或者最好用if __name__ == '__main__'
# if __name__ == '__main__':
#     for i in range(600):
#         print('********************')
#         tB.apply_async((i,))