select
    actor_id, first_name || last_name as full_name
from {{ source("source", "actor") }}
