"""
Simple repository that contains our parallel pipeline.
"""
import sys

from dagster import repository
from dagster.utils import script_relative_path

sys.path.append(script_relative_path("."))

from celery_pipeline import parallel_pipeline
from single_solid_pipeline import hello_cereal_pipeline

@repository
def test_repository():
    return [parallel_pipeline, hello_cereal_pipeline]
