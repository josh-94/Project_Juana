# Project Chatbot - Juana by Teoma
The juana by teoma project corresponds. Create a chatbot to provide information at any time and provide order statuses to customers. An API linked to the Sendpulse chatbot platform was created. With them we can have all the communication links.

#### Functionalities:
* Record order status
* Show order status
* Show products archive
* Contact a personal advisor

## Table of Content
* [Environment] (#environment)
* [Installation] (#installation)
* [File Descriptions] (#file-descriptions)
* [Examples of use] (#examples-of-use)
* [Authors] (#authors)
* [License] (#license)

## Environment
This project is interpreted/tested on Ubuntu 20.4 LTS using python3,Flask, json web token, mysql, bootstrap y javascript.

## Installation
* Clone this repository: `git clone "https://github.com/josh-94/Project_Juana.git"`
* Access Project_Juana directory: `cd Project_Juana`
* Run app.py: `./app.py`

# Backend

## File Descriptions
[app.py](app.py) - The Main file where it houses the routes and the connections of the project:
* `app` - Name of proyect
* `cors` - API route router
* `load_dotenv` - development or production checker

[config.py](config.py) - File where it saves all the configuration of the project connections:
* `ProductionCOnfig` - Database Credentials Consultant

[function_jwt.py](function_jwt.py) - File where the parameters and the established times of the token are configured for the queries of our API:
* `expire_date` - Time of expire
* `write_token` - write according to the parameter
* `Validate_token` - Validation of token

# Base of Data

## File Descriptions
[Tables](tables) - Script of the creation of all the tables
[Procedures](Procedures) - Creation of procedures for storage of API requests.

# Frontend

