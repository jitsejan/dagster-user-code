"""
https://docs.dagster.io/tutorial/intro-tutorial/single-solid-pipeline
"""
import requests
import csv
from dagster_celery_k8s import celery_k8s_job_executor
from dagster import ModeDefinition, default_executors, pipeline, solid

celery_mode_defs = [ModeDefinition(executor_defs=default_executors + [celery_k8s_job_executor])]

@solid
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")

    return cereals

@pipeline(mode_defs=celery_mode_defs)
def hello_cereal_pipeline():
    hello_cereal()
