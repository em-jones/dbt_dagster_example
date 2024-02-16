FROM python:3.10-slim

# TODO: Probably a case where we'd want to just build prior to mounting
RUN apt-get update -y && apt install git -y

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagster-webserver and dagster-daemon, and to load the DagsterInstance

# Add repository code

WORKDIR /opt/dagster/app
COPY ./pyproject.toml ./setup.py ./
ENV DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1
RUN pip install -e ".[dev]"

COPY ./dbt_project/dbt_project.yml  ./dbt_project/dbt_project.yml
COPY ./dbt_project/profiles.yml  ./dbt_project/profiles.yml
RUN dbt deps --project-dir /opt/dagster/app/dbt_project

COPY ./ /opt/dagster/app


# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "code-server", "start", "-h", "0.0.0.0", "--working-directory", "/opt/dagster/app",  "-p", "4000", "--module-name", "orchestration.definitions"]
