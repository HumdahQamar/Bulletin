# Top 5 news articles from New York Times
An application that fetches articles from the NYTimes Article Search API.

## Getting Started

### Prerequisites
All required libraries are listed under ```requirements.txt```

### Installation
It is a good idea to install all project dependencies in a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/).

Install all relevant libraries and dependencies by executing the following command in the project root directory:
```shell
pip install -r requirements.txt
```

## Starting the server
Run the following command from the ```root``` directory of your project to run the server on your local machine
```shell
python manage.py runserver
```
The default port for the application is ```8000```

To create a super user, run
```shell
python manage.py cratesuperuser
```
## Admin Site
In order to access the admin site, navigate to ```localhost:8000/admin```
This is where queries can be searched, added, removed and updated

## Built with
* [Django](https://docs.djangoproject.com/en/2.1/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* HTML5, Bootstrap

## Author
[Humdah Qamar](https://github.com/HumdahQamar)
