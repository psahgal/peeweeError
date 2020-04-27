# peeweeError

This repository illustrates what appears to be a regression in the [Peewee Python
library](http://docs.peewee-orm.com/en/latest/) from version 3.13.1 to version 3.13.3. It uses
[PostgreSQL](https://www.postgresql.org/) for its database. The issue involves setting up a relationship with a foreign
key before writing multiple rows for different entities to the database with the `bulk_create` function.

This was tested on Python 3.8.2.

[Here](https://github.com/coleifer/peewee/issues/2162) is the issue associated with this example.

## Usage
1. Install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/),
   if you don't have it already. This will be used to run the database instance.
2. In a separate termianl window, run `docker-compose up` in the root directory. This will start up the database
   instance.
3. Install either the working library version or the failing library version with `pip install -r
   working_requirements.txt` or `pip install -r failing_requirements.txt`, respectively.
4. Run `python main.py`. With the working requirements, the test passes, and a few tables and rows are added to the
   database.