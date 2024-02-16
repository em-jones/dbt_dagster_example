import os

from dagster import (AssetSelection, Definitions, ScheduleDefinition, asset,
                     define_asset_job, in_process_executor)
from dagster_dbt import DbtCliResource, build_schedule_from_dbt_selection

from .airbyte import airbyte_assets
from .dbt import actors, dbt_project_dir

schedules = [
    build_schedule_from_dbt_selection(
        [actors],
        job_name="materialize_dbt_models",
        cron_schedule="0 0 * * *",
        dbt_select="fqn:*",
    ),
]

dbt_cli_resource = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

ems_etl_job = define_asset_job(
        "ems_etl_job", 
        AssetSelection.groups("actors").upstream().required_multi_asset_neighbors(),
        executor_def=in_process_executor,
        )

@asset
def sync():
    return airbyte_assets

defs = Definitions(
    assets=[airbyte_assets, actors],
    resources={
        "dbt": dbt_cli_resource
    },
    schedules=[

        ScheduleDefinition(
            job=ems_etl_job,
            cron_schedule="* * * * *"
            )
        ]
)
