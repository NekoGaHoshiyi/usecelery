from kombu import Exchange, Queue
from celery.schedules import crontab
from datetime import timedelta


BROKER_URL = "redis://192.168.132.128:6379/1"
CELERY_RESULT_BACKEND = "redis://192.168.132.128:6379/3"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 24*3600
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = "Asia/Shanghai"

CELERYD_MAX_TASKS_PER_CHILD = 400
CELERYD_MAX_MEMORY_PER_CHILD = 300000

# 不限是包还是py文件，目录下或文件内一定要能找的到实例，具体找的就是创建完成的实例而不是@语法糖施加的任务
CELERY_IMPORTS = (
    "gen_celery",
)

CELERY_QUEUES = (
    Queue("taskA_queue", Exchange("taskA_queue"), routing_key="taskA_queue"),
    Queue("taskB_queue", Exchange("taskB_queue"), routing_key="taskB_queue"),
    Queue("noname", Exchange("noname"), routing_key="noname"),
)

# 不限是包还是py文件，目录下或文件内一定要能找的到任务，具体找的就是@语法糖施加的任务
# 决定的是任务和队列的接管关系
CELERY_ROUTES = {
    "taskA.*": {"queue": "taskA_queue", "routing_key": "taskA_queue"},
    "taskB.*": {"queue": "taskB_queue", "routing_key": "taskB_queue"},
    "noname.*": {"queue": "noname", "routing_key": "noname"},
}

