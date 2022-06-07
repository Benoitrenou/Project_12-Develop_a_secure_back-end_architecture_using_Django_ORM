In this scenario, EpicEvents wants to develop an API that will serve as a CRM

The Entity-Relationship diagram must be built before moving to the API via Django REST

This application was built using Django Rest Framework in its version 3.13.1.

Objectives of the project:
  - Build an Entity-Relationships diagram
  - Build models of the application base on client work descritpion
  - Configure a database via PostgreSQL and integrate it to Django settings
  - Customize the administration interface of the application

## Entity-Relationships diagram

You can access the diagram in the file diagramme_epic_events_crm.jpg 

## Create virtual environment

From your terminal, enter the following commands depending on your operating system

### With Linux/ MAC OS

    $ python -m venv <environment_name>
    example : python -m venv venvAPI
    
### With Windows:
    
    $ virtualenv <environment_name>
    example : virtualenv venvAPI 
    
## Activate virtual environment

### With Linux / MAC OS:

    $ source <environment_name>/bin/activate
    example : source venvAPI/bin/activate
   
### With Windows:

    $ source <environment_name>/Scripts/activate
    example : source venvAPI/Scripts/activate
    
## Installation of packages : 

    $ pip install -r requirements.txt

## Launch application

    $ python manage.py runserver

## Documentation

You can find the documentation of the API [at this address](https://documenter.getpostman.com/view/17414272/UVknsb7L)