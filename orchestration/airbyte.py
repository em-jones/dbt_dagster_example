from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance

airbyte_server = AirbyteResource(
    host="airbyte-proxy", port="8000", username="airbyte", password="password"
)

airbyte_assets = load_assets_from_airbyte_instance(
        airbyte_server, 
        connection_filter=lambda meta: "em" in meta.name ) # NOTE: how I load the correct "sync" from airbyte


