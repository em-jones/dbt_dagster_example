from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance
from .config import airbyte_password, airbyte_connections

airbyte_server = AirbyteResource(
    host="airbyte-proxy", port="8000", username="foley-rnd", password=airbyte_password
)

airbyte_assets = load_assets_from_airbyte_instance(
        airbyte_server, 
        connection_filter=lambda meta: airbyte_connections in meta.name ) # NOTE: how I load the correct "sync" from airbyte
