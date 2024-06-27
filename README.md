# Website

This repository contains the Django application which powers TBA.

## What's in it?

It's a blogging site that relies on [Django Blog Improved](https://github.com/cameronnicolson/django-blog-improved) as it's CMS.

## Requires

* `Python 3.6` or any version above

* Django `3.2.12`

* PostgreSQL `9.5` and higher

## Install 

## PostgreSQL

Website can automatically populate the database with the relevant tables and indexes, but it is not capable of creating the databases themselves. You will need to create the databases manually.

### Create a new PostgreSQL user

Create a user which Website can use to connect to the database, choosing a new password when prompted. On some *nix systems, you may need to leave out the `sudo -u` part from the below instructions.

```
sudo -u postgres createuser -P django
```

### Create a postgresql database
Create the database itself, using the django user from above. `-0` flag is the owner followed by the database name.

```
sudo -u postgres createdb -O django blog
```

Run the migration to create database schema:

```
python manage.py makemigrations
```

Apply schema to database:

```
python manage.py migrate
```

### Create testing database 

Django will use a different database for running tests. Privileges will need to be assigned to allow database creation. 

Assuming your username is django, grant permissions like with psql shell:

```
sudo -u postgres psql -c 'ALTER USER django CREATEDB;'
```

# License

![AGPLv3 Logo](https://www.gnu.org/graphics/agplv3-155x51.png "AGPLv3 Logo")

All files are copyright of 2024 Cameron Nicolson, unless stated otherwise.

Django Blog Improved is released under AGPLv3. 
We conventionally placed the license in a file called [LICENSE](./LICENSE).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).
