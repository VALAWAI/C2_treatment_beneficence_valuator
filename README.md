# C2_treatment_beneficence_valuator

The C2 treatment beneficence valuator check that the treatments to be applied over
a patient follows the beneficence_value.

## Summary

 - Type: C2
 - Name: Treament beneficence valuator
 - Version: 1.0.0 (January 13, 2025)
 - API: [1.0.0 (January 13, 2025)](https://raw.githubusercontent.com/VALAWAI/C2_treatment_beneficence_valuator/ASYNCAPI_1.0.0/asyncapi.yml)
 - VALAWAI API: [1.2.0 (March 9, 2024)](https://raw.githubusercontent.com/valawai/MOV/ASYNCAPI_1.2.0/asyncapi.yml)
 - Developed By: [IIIA-CSIC](https://www.iiia.csic.es)
 - License: [GPL 3](LICENSE)


## Generate Docker image

The easy way to create the docker image of this component is to execute
the next script.
 
 ```
./buildDockerImages.sh
```

In the end, you must have the docker image **valawai/c2_treatment_beneficence_valuator:Z.Y.Z**
where **X.Y.Z** will be the version of the component. 

This script has the next parameters.

 * **-nc** or **--no-cache** Build a docker image without using the cache.
 * **-t <tag>** or **--tag <tag>** Build a docker image with a the **<tag>** name.
 * **-p <platforms>** or **--platform <platforms>** Specify the architectures to build the docker.
 * **-dp** or **--default-platforms** Uses the default platforms (linux/arm64, linux/amd64).
 * **-h** or **--help** Show a help message that explains these parameters.

For example the next call can be used to generate the image with the tag **latest**.

```
./buildDockerImages.sh -t latest
```

And you will obtain the container **valawai/c2_treatment_beneficence_valuator:latest**.


### Docker environment variables

The most useful environment variables on the docker image are:

 - **RABBITMQ_HOST** is the host where the RabbitMQ is available.
 The default value is **mov-mq**.
 - **RABBITMQ_PORT** defines the port of the RabbitMQ.
 The default value is **5672**.
 - **RABBITMQ_USERNAME** contains the username of the user who can access RabbitMQ.
 The default value is **mov**.
 - **RABBITMQ_PASSWORD** is the password used to authenticate the user who can access the RabbitMQ.
 The default value is **password**.
 - **RABBITMQ_MAX_RETRIES** is the maximum number of tries to connect to the RabbitMQ.
 The default value is **100**
 - **RABBITMQ_RETRY_SLEEP** is the seconds to wait before the component tries to connect again with the RabbitMQ.
 The default value is **3**
 - **LOG_CONSOLE_LEVEL** defines the level of the log messages to be shown in the console.
 The possible values are CRITICAL, FATAL, ERROR, WARN, WARNING, INFO or DEBUG. The default value is **INFO**.
 - **LOG_FILE_LEVEL** defines the level of the log messages to be stored in the log file.
 The possible values are CRITICAL, FATAL, ERROR, WARN, WARNING, INFO or DEBUG. The default value is **DEBUG**.
 - **LOG_FILE_MAX_BYTES** defines the maximum number of bytes the log file can have before rolling.
 The default value is **1000000**.
 - **LOG_FILE_BACKUP_COUNT** defines the maximum number of rolling files to maintain.
 The default value is **5**.
 - **LOG_DIR** defines the directory to store the maximum number of rolling files to maintain.
 The default value is **logs**.
 - **LOG_FILE_NAME** defines the file name at the **LOG_DIR** where the log messages will be stored.
 The default value is **c2_treatment_beneficence_valuator.txt**.
 - **COMPONET_ID_FILE_NAME** defines the file name at the **LOG_DIR** where the component identifier,
 obtained when the component is registered in the MOV, will be stored.
 The default value is **component_id.json**.
 

### Docker health check

When this component is registered, it stores the registered result in the file
**/app/${LOG_DIR:-logs}/${COMPONET_ID_FILE_NAME:-component_id.json}**. Also,
when the component is unregistered, this file will removed.  Thus, you can check
the size of this file to know if the component is ready. For example, you can add the following
configuration to a **docker compose** to check if the component is healthy.

```
    healthcheck:
      test: ["CMD-SHELL", "test -s /app/logs/component_id.json"]
      interval: 1m
      timeout: 10s
      retries: 5
      start_period: 1m
      start_interval: 5s
```


## Deploy

After you have the **valawai/c2_treatment_beneficence_valuator:latest** docker image you can deploy
this component using the docker compose using the file [docker-compose.yml](docker-compose.yml)
defined on the [repository](https://github.com/VALAWAI/C2_treatment_beneficence_valuator).

This configuration defines the profile **mov** to launch the component at the same time that a 
 [Master of valawai (MOV)](/tutorials/mov). You can use the next
command to start both.

```
COMPOSE_PROFILES=mov docker compose up -d
```

After that, if you open a browser and go to [http://localhost:8080](http://localhost:8080)
you can view the MOV user interface. Also, you can access the RabbitMQ user interface
at [http://localhost:8081](http://localhost:8081) with the credentials **mov:password**.

The docker compose defines some variables that can be modified by creating a file named
[**.env**](https://docs.docker.com/compose/environment-variables/env-file/) where 
you write the name of the variable plus equals plus the value.  As you can see in
the next example.

```
MQ_HOST=rabbitmq.valawai.eu
MQ_USERNAME=c2_treatment_beneficence_valuator
MQ_PASSWORD=lkjagb_ro82t¿134
```

The defined variables are:


 - **C2_TREATMENT_BENEFICENCE_VALUATOR_TAG** is the tag of the C2 Treatmentbeneficence 
 valuator docker image to use. The default value is **latest**.
 - **MQ_HOST** is the hostname of the message queue broker to use.
 The default value is **mq** which is the server started in the compose.
 - **MQ_PORT** is the port of the message queue broker is available.
 The default value is **5672**.
 - **MQ_UI_PORT** is the port of the message queue broker user interface is available.
 The default value is **8081**.
 - **MQ_USER** is the username that can access the message queue broker.
 The default value is **mov**.
 - **MQ_PASSWORD** is the password used to authenticate the user who can access the message queue broker.
 The default value is **password**.
 - **RABBITMQ_TAG** is the tag of the RabbitMQ docker image to use.
 The default value is **management**.
 - **MONGODB_TAG** is the tag of the MongoDB docker image to use.
 The default value is **latest**.
 - **MONGO_PORT** is the port where MongoDB is available.
 The default value is **27017**.
 - **MONGO_ROOT_USER** is the name of the root user for the MongoDB.
 The default value is **root**.
 - **MONGO_ROOT_PASSWORD** is the password of the root user for the MongoDB.
 The default value is **password**.
 - **MONGO_LOCAL_DATA** is the local directory where the MongoDB will be stored.
 The default value is **~/mongo_data/movDB**.
 - **MOV_DB_NAME** is the database name used by the MOV.
 The default value is **movDB**.
 - **MOV_DB_USER_NAME** is the name of the user used by the MOV to access the database.
 The default value is **mov**.
 - **MOV_DB_USER_PASSWORD** is the user password used by the MOV to access the database.
 The default value is **password**.
 - **MOV_TAG** is the tag of the MOV docker image to use.
 The default value is **latest**.
 - **MOV_UI_PORT** is the port where the MOV user interface is available.
 The default value is **8080**.
 - **LOG_LEVEL** defines the level of the log messages to be shown in the console.
 The possible values are CRITICAL, FATAL, ERROR, WARN, WARNING, INFO or DEBUG. The default value is **INFO**.


The database is only created the first time that the script is called. So, if you modify
any of the database parameters you must create the database again. For this, you must
remove the directory defined by the parameter **MONGO_LOCAL_DATA** and start again
the **docker compose**.

You can stop all the started containers with the command:

```
COMPOSE_PROFILES=mov docker compose down
```
  
## Development

You can start the development environment with the script:

```shell script
./startDevelopmentEnvironment.sh
```

After that, you have a bash shell where you can interact with the Python code. You can use the next command
to so some common action.

* **run** to start the component.
* **testAll** to run all the unit tests
* **coverage** to run all the unit tests and obtain its coverage.
* **test test/test_something.py** to run the tests defined on the file **test_something.py**
* **test test/test_something.py::TestClassName::test_do_something** to run the test named **test_do_something** defined on the class **TestClassName** defined in the file **test_something.py**

Also, this starts the tools:

 * **RabbitMQ** is the server that manages the message brokers.
 The management web interface can be opened at **http://localhost:8081** with the credential
 **mov**:**password**.
 * **MongoDB** is the database used by the MOV. The database is named **movDB** and the user credentials **mov:password**.
 The management web interface can be opened at **http://localhost:8081** with the credential
 **mov**:**password**.
 * **Mongo express** is the web interface to interact with the MongoDB. The web interface
 can be opened at **http://localhost:8082**.
 * **Master Of VALAWAI (MOV)** the web interface to interact with the Master Of VALWAI(MOV). The web interface
 can be opened at **http://localhost:8083**.


## Links

 - [C2 Treament beneficence valuator documentation](https://valawai.github.io/docs/components/C2/treatment_beneficence_valuator)
 - [Master Of VALAWAI tutorial](https://valawai.github.io/docs/tutorials/mov)
 - [VALWAI documentation](https://valawai.github.io/docs/)
 - [VALAWAI project web site](https://valawai.eu/)
 - [Twitter](https://twitter.com/ValawaiEU)
 - [GitHub](https://github.com/VALAWAI)
 