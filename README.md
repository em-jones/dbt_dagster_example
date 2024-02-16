# Accessing Server Using VSCode


## Common Activities:

### CLI
#### Deploy your Dagster service
   - `make run` - runs your [`dagster`](#dagster) project
   - `make watch` - runs your [`dagster`](#dagster) project as a hot-reloading service
#### Access 
  - `make pg_access_info` - prints the database connection information
  - `make redshift_access_info` - (Jeff-specific) - prints redshift connection information

### VSCode

#### SQLTools

If you want to connect to your data stores(Postgres/Redshift)

![SQLTools](image.png)

#### DBT Power User

DBT Power Tools is a VSCode extension that should help with the operations common to DBT projects.
[More info](https://www.dbt-power-user.com/)
![alt text](image-1.png)

#### Port-Forwarding

The project is configured to port-forward ports `3000`(Dagster) and `8000`(Airbyte)

![alt text](image-2.png)

### [Dagster](./orchestration/README.md)

To view the results of your `Dagster` deployment(`make run` / `make watch`)

- located at `localhost:3000`
- managed by`./orchestration/` project

### [Airbyte](./orchestration/README.md#airbyte)
- located at `localhost:8000`

### [dbt](./dbt_project/README.md)
- managed by the `./dbt_project/` project

### Databases
Each user has two databases available.
Each database is named using the *first name* of the user, all in lower-case; e.g. "Em" -> "em"

#### Source
- postgres
- host: `localhost`
- port: `5432`
- credentials: [See note about accessing](#Access)
- [data available](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)
- [jeff's database - job_skills table(for redshift testing)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024?select=job_skills.csv)

#### Destination
- postgres
- host: `localhost`
- port: `6543`
- credentials: [See note about accessing](#Access)

