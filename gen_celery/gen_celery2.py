from celery import Celery

celeryA = Celery()
celeryB = Celery()
celeryC = Celery()

celeryA.config_from_object('celery_configA')
celeryB.config_from_object('celery_configA')
celeryC.config_from_object('celery_configA')
