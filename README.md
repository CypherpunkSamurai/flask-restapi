# Geo-Twitter
![python-badge](https://img.shields.io/badge/python-3.10-blue?style=flat&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/Flask-2.2-blue?style=flat&color=lightgrey&logo=flask&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-blue?style=flat&logo=postgresql&logoColor=white)
![openweathermap](https://img.shields.io/badge/OpenWeatherMap-blue?style=flat&color=orange)  

A Twitter Backend Clone using Python3 Flask.

### Easy Deploy and Testing

A demo rest api endpoint is listed below. You can also Consider using the buttons below for easy deployment and testing the demo endpoint.

- **Demo Inference URL:**  
  - `https://pythoninternship.rakeshs.eu.org/` - [\[visit\]](https://pythoninternship.rakeshs.eu.org/)  
  - `https://flask-restapi-production.up.railway.app/` - [\[visit\]](https://flask-restapi-production.up.railway.app/)

- **Test the Demo API:**  
  [![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Python%20SDE%20Internship%202023&uri=https%3A%2F%2Fgithub.com%2FCypherpunkSamurai%2Fflask-restapi%2Fblob%2Fmaster%2Fdocs%2Frest_api_definition.insomnia.json)


- **Deploy this API:**  
  [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/J6Czq1)

## Installation

### Requirements

To install the application you will require:
- python 3.10
- `poetry` or `pip`

## Instructions

To install the flask server we need to clone the repository first.
```shell
git clone https://github.com/CypherpunkSamurai/flask-restapi.git 
```

Then install the python3 requirements using `pip` or `poetry`:

```shell
cd flask-restapi
pip install -r requirements.txt
```

Then configure the server using environment variables:  

```shell
# Your Postgres Database URL
POSTGRES_URL="postgresql://<user>:<password>@<host>:5432/<database>"

# Your Open Weather Map API Key
OPENWEATHERMAP_KEY="...."

# Server Host
# (OPTIONAL Required in Cloud Deployments)
export HOST="0.0.0.0"

# Server Port
# (OPTIONAL Required in Cloud Deployments)
export PORT=5000

# Create the tables and required functions
# ( OPTIONAL For Database Migrations,
#   i.e. running on a new database )
export CLEAN_START=True
```
**Note:** You can use a `.env` file to configure the server as well.

### Running the Server

Running the server requires you to type the command:

```shell
python run.py
```

The server should be running!

## Credits
- **Python3 Flask** - For the wonderful framework
- **Flask SQLalchemy** - For the wonderful flask integration 
- **OpenWeather API** - For the Free Weather API
- **PostgreSQL** - For Providing extendable database
