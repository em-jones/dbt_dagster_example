# Orchestration

This portion of the codebase is responsible for *orchestrating* the *data workloads*
in a system.

Specifically, this is where the dagster codebase lives.

## TL;DR

This is likely a space where the data *platform* team members are spending time. As well, it's not something that's likely to have a lot of change once we understand the patterns we want to support.

That said, it's probably useful to have a look at a couple of lines:
- [How dagster selects *assets*(see "Core Concepts") from airbyte](./airbyte.py#L9)

## Dagster
Workload orchestration platform *purpose-built* for data operations.

Dagster goes beyond running jobs and logging outputs to help with the documentation of those
workloads through visualization of data lineage and the surfacing of lower-level data documentation.

### [Core Concepts](https://docs.dagster.io/concepts)
