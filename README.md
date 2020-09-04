# chess-bot

Install pre-requisites
----------------------

1. Python 3
2. Virtualenv with virtualenvwrapper
3. PostgresSQL
4. ngrok

Local project initialization
----------------------------

1. Clone repo: `git clone git@github.com:DzesenKopeykin/chess-bot.git`
2. Create virtual environment: `mkvirtualenv chess_bot`
3. Install requirements: `pip install -r requirements/local.txt`
4. Create your own [developer Bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) on Telegram
5. Edit `$VIRTUAL_ENV/bin/postactivate`:

        export BOT_TOKEN={{ your_bot_token }}
        export DB_NAME={{ your_database_name }}
        export DB_USER={{ your_database_user }}
        export DB_PASSWORD={{ your_database_password }}

6. Re-activate environment `workon chess_bot`
7. Create local database:

        sudo -u {{ your_database_user }} psql
        CREATE DATABASE {{ your_database_name }};
        \q

8. Run migrations: `./manage.py migrate`
9. Create superuser for Django CMS: `./manage.py createsuperuser`
10. Unzip ngrok file to root of project 

How to start bot locally
-----------

1. Run `./tunnel.sh`
2. Run `workon chess_bot`
2. Run `python3 set_webhook.py`
3. Run `./manage.py runserver`