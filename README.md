# Project Chatbot - Juana by Teoma
![JUANA](https://github.com/josh-94/Project_Juana/blob/main/fronted_Juana/src/static/img/logoJuana.png)

### Descripción
***
Juana by teoma. Is a company that sells cannabis-based medicinal products, it has a great job before society to eliminate all negative stigma towards silver, in a country where only medicinal use is allowed, but with very little information and that highlights all its properties. The company has three product lines where the customer can choose according to their needs. Juana is linked to the company Teoma, it is a Peruvian multilevel company with a presence in more than 5 countries where its clients are called partners, through a single payment they have access to supplier discounts and new partners can sell their products to their clients. That is why in Juana only people registered as members of Teoma can buy.

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

### `models` directory contains classes used for this project:

[entities](entities) - Login validation:
* `User` - Class user for credentials
* `ModelUser` - Conexion and validate user
* `get_by_id` - Call database for table user

### `Static` directory contains style and image for this project:

[css](css) - Style css:
* `home` - style of home
* `login` - Styyle of home

[img](img) - Images

### `Templates` directory contains templates of bootstrap:
[base.html](base.html) - Template base

[home.html](home.html) - Template home

# Requirements

### `Requirements` All the requirements are met to be able to start the project.

## Examples of use
```
Ubuntu_Juana$./app.py

(env)Ubuntu_Juana$: curl http://3.84.55.178:5000/trasmitirEstado
================================================================
{
  "numeroGuia" : "DEV1141541414078-05",
  "numeroPedido" : "1141541414078-05",
  "estado" : "14",
  "lugar" : "Dueños/consignatario",
  "quienRecibe" : ""Sofia Hinojosa",
  "motivoDescripcion" : "",
  "fecha" : "15:00",
  "hora" : "https://..../77695057e8c.png",
  "observacion" : ""
}
```
### Response

```
Ubuntu_Juana$:
==================================================================
{
  "codigo" : "1",
  "mensaje" : "Se registró correctamente"
}

OR

{
  "codigo" : "0",
  "mensaje" : "No se pudo registrar"
}
```
## Author
Jeshua Cabanillas - [Github](https://github.com/josh-94) / [LinkedIn](https://www.linkedin.com/in/jeshuacabanillas/)

Diego Morey - [Github](https://github.com/DAlons27) / [LinkedIn](https://www.linkedin.com/in/admorey/)

Giuliano FLores - [Github](https://github.com/mrgiulls) / [LinkedIn](https://www.linkedin.com/in/giuliano-flores-mesias/)

Ronald Altamirano - [Github](https://github.com/ronLabs) / [LinkedIn](https://www.linkedin.com/in/ron-altamirano/)

## License
Public Domain. No copy write protection. 
