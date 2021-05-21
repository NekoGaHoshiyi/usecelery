from celery import Celery

celeryA = Celery()
celeryB = Celery()
celeryA.config_from_object('celery_configA')
celeryB.config_from_object('celery_configB')
