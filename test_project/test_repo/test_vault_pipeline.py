import os
from dagster_celery_k8s import celery_k8s_job_executor
from dagster import ModeDefinition, default_executors, pipeline, solid
from hvac import Client

celery_mode_defs = [ModeDefinition(executor_defs=default_executors + [celery_k8s_job_executor])]

@solid
def get_test_secret(context):
    client = Client(
        url=os.environ['VAULT_URL'],
        token=os.environ['VAULT_TOKEN'])
    read_response = client.secrets.kv.v2.read_secret_version(path='jjsamplesecrets')
    result = read_response.get('data').get('data').get('my-key')
    context.log.info(f"Found the value {result}")
    return result

@pipeline(mode_defs=celery_mode_defs)
def get_test_secret_pipeline():
    get_test_secret()
