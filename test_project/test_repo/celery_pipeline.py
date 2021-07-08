"""
A basic pipeline that can be executed with Celery.
"""
from dagster_celery_k8s import celery_k8s_job_executor
from dagster import ModeDefinition, default_executors, pipeline, solid

celery_mode_defs = [ModeDefinition(executor_defs=default_executors + [celery_k8s_job_executor])]

@solid
def not_much(_):
    return

@pipeline(mode_defs=celery_mode_defs)
def parallel_pipeline():
    for i in range(5):
        not_much.alias("not_much_" + str(i))()
