from setuptools import find_packages, setup


setup(
    name="orchestration",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-dbt",
        "dagster-airbyte",
        "dagster-docker",
        "dagster-postgres",
        "dbt-postgres",
        "dbt-redshift"
    ],
)
