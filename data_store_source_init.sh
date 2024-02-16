#!/bin/bash
set -e
users=(husam em david maggie scott alan joe jeff)

# Create users
printf '%s\n' "${users[@]}"  | xargs -I % bash -c 'psql -v ON_ERROR_STOP=1 --username postgres -h 0.0.0.0  --dbname postgres <<-EOSQL
	CREATE USER $1;
	CREATE DATABASE $1;
	GRANT ALL PRIVILEGES ON DATABASE $1 TO $1;
EOSQL' - %

# Import Data for each user
printf '%s\n' "${users[@]}"  | xargs -I % bash -c 'pg_restore -U postgres -Ft -d $1 dvdrental.tar' - %

psql -U postgres -h 0.0.0.0 --dbname jeff <<-EOSQL
CREATE TABLE skills (
  job_link VARCHAR(510),
  job_skills VARCHAR(25500)
);
COPY skills(job_link, job_skills)
FROM '/job_skills.csv'
DELIMITER ','
CSV HEADER;
EOSQL
