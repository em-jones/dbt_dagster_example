select
    actor_id,
    last_name,
    first_name,
    first_name || last_name as full_name,
    last_update
from {{ source("sync", "actor") }}
