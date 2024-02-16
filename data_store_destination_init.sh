#!/bin/bash
set -e

set -e
users=(husam em david maggie scott alan joe)

# Create users
printf '%s\n' "${users[@]}"  | xargs -I % bash -c 'psql -v ON_ERROR_STOP=1 --username postgres -h 0.0.0.0  --dbname postgres <<-EOSQL
	CREATE USER $1;
	CREATE DATABASE $1;
	GRANT ALL PRIVILEGES ON DATABASE $1 TO $1;
EOSQL' - %
