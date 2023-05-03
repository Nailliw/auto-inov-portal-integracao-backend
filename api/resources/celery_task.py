from time import sleep

from api import factory

celery = factory.celery


@celery.task()
def asynchronous(name):
    """Async long task method."""
    sleep(5)
    return {'async': name}


asynchronous = asynchronous
