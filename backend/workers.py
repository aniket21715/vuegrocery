from celery import Celery
from flask_caching import Cache
cache = Cache()

# celery_app = Celery('Application Jobs')

# if __name__ == '__main__':
#     celery_app.start()

   

def make_celery(app):
    celery = Celery(
        'Application Jobs',
        broker_url='redis://localhost:6400/1',
        result_backend='redis://localhost:6400/2',
        broker_connection_retry_on_startup=True,
        CELERY_TIMEZONE = "Asia/Kolkata"
    )
    
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery
