The tech task for the Bluetel hiring. This file will instruct how to use this sample program.

The application is developed in [Docker](https://www.docker.com) and [Docker compose](https://docs.docker.com/compose/) technologies. Please install those into your environment before your test/run.

Makefile
----
If your platform supports the "make" command, the simplest way to execute the app is:
```bash
git clone https://github.com/kensonman/hiring
cd hiring/API
make clean test #for testing
make clean run #for launching the test server
```

Docker
----
To build and execute the image, simply run the following commands:
```bash
git clone https://github.com/kensonman/hiring
cd hiring/API
docker build -t hiring:kenson .
docker run --rm --name test  hiring:kenson /usr/src/app/start test #for testing
docker run --rm --name test -p 5000:5000 hiring:kenson /usr/src/app/start run #for launch the testing service
```

Environment Variable
----
All the runtime variables are store in .env file. 
```
HOST=kenson.idv.hk
PORT=5000
DBENGINE=django.db.backends.sqlite3
DBNAME=bluetel.sqlite
DBUSER=
DBPORT=
DBPASS=
```
