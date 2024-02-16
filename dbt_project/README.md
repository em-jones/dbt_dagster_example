# DBT Project

## TL;DR

- DBT is *effectively* a replacement for stored procedures
  - [~10 minute read about migrating](https://docs.getdbt.com/blog/migrating-from-stored-procs) (should clarify some of the analagous concepts)
- A lot of your time will be spent in `./models/` directory
- `.sql` files found in `./models/` directory get *materialized* as tables or views based on how it's been configured in [`./dbt_project.yml`](./dbt_project.yml) - [more information](https://docs.getdbt.com/docs/build/materializations)
- the [sources](./models/sources.yml) config accomplishes a couple of things:
    - tells our models(`.sql` files) where data comes from (declared by [source()](./models/actors/with_full_name.sql#L3))
