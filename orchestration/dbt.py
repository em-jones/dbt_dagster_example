# NOTE: *probably* out of scope for learning activities

import os
from pathlib import Path

from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

dbt_project_dir = Path(__file__).joinpath("../..", "dbt_project").resolve()
dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))


if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt_parse_invocation = dbt.cli(["parse"], manifest={}).wait()
    dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")


@dbt_assets(manifest=dbt_manifest_path)
def actors(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
