Intro
====
This file provide the basic information of the tech which I selected on this project. And also provide the basic information of each technologies.

I selected the Python + Django (with Django REST framework) + SQLite to fulfill the requirements. 

I had also selected the [Docker](https://www.docker.com/) and [Docker-compose](https://docs.docker.com/compose/) as the development and testing platform. The docker compose can build and prepare the testing platform according to the environment description (a YAML file).

Python
----
The [Python](https://www.python.org/downloads/release/python-379/) is one of the popular scripting languages. This is suitable for the small scale and provide the excellent development speed.

The project size is the main reason of selecting Python as the programming language. This is one of my favorite programming language and I loved to development in it.

Django
----
The [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. That include all the necessary components (URL routing, request/response handling, data presistenacy, etc.)

The [Django REST framework](https://www.django-rest-framework.org/) is one of the popular framework that extends the Django to support/dealing with the web API.

I use the Django to building the data-model, URL routing and view-controlling.

SQLite
----
SQLite is the lightweight database that store all the information in a signal binary file. That support [almost all features](https://www.sqlite.org/fullsql.html) of SQL language.

That is the most quickly way to build the database for the Django without any configuration.

This is not suitable for production environment but the development. Just because all the data stored into a signal file (may be in the docker node).

To switch to production environment, it is strongly recommended that to swap to mature database system (such as PostgreSQL, MySQL, MongoDB, etc.). This is also included in the Django framework. We can deploy it with [simple configuration](https://pythonfusion.com/switch-database-django/).
