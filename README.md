# django_swagger

### Pré-requisitos

Before starting, you will need to have the following tools installed on your machine:
[Git](https://git-scm.com), [Python](https://www.python.org/downloads/). Besides, it's good to have an editor to work with the code like [VSCode](https://code.visualstudio.com/)

---

### 🎲 Running the server

```bash
# Clone this repository
$ git clone <https://github.com/caiquilipe/django_swagger.git>

# Access the project folder in terminal/cmd
$ cd django_swagger

# Create an env environment
$ python -m venv env

# Active o env
$ source env/bin/activate

# Install the dependencies
$ pip install -r requirements.txt

# Run the makemigrations
$ python manage.py makemigrations

# Run the migrate
$ python manage.py migrate

# Run the application
$ python manage.py runserver
