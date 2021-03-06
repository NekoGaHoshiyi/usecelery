from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/1',
             broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


@app.task  # 普通函数装饰为 celery task
def add(x, y):
    return x + y

for i in range(10):
    add.apply_async((i, i+1))