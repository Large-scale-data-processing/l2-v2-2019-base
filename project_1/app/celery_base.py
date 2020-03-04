from celery import Celery
from docker_logs import get_logger
logging = get_logger("task")

app = Celery()

@app.task(bind=True, name='task')  
def task(self, param):  
    logging.info(f"Celery task executed with param: {param}")
    return f"Result of task for param {param}"
  