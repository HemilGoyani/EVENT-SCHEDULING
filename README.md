# EventScheduling

## Setup the project

### Clone the project from git repository and move into the project directory.

```sh
git clone https://github.com/HemilGoyani/EVENT-SCHEDULING.git
cd EVENT-SCHEDULING/
```

### Create and Activate virtual environment

```sh
python -m venv venv
source venv/bin/activate
```

### Install requirements.txt file with this command.

```sh
pip install -r requirements.txt
```

### Create .env file

```sh
cp .env.template .env
```

### Migrate the file command
python manage.py migrate

### Run the Project command

python manage.py runserver 0.0.0.0:8000
