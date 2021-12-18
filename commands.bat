REM migrate : looks at the INSTALLED_APPS setting and creates database tables (settings.py)
python manage.py migrate

REM makemigrations : store changes to the models (and thus the db schema) as a migration (CREATE MIGRATIONS)
REM polls/migrations/0001_initial.py 
python manage.py makemigrations polls

REM sqlmigrate: takes migration names and returns their SQL
REM !! The sqlmigrate command doesn’t actually run the migration on the database 
REM instead, it prints to the screen what SQL Django thinks is required
REM RUN migrate to create those model tables in the database
python manage.py sqlmigrate polls 0001

REM check : check for problems without making changes 
python manage.py check

REM migrate : command that will run the migrations and manage the database schema automatically
REM takes all the migrations that haven’t been applied and runs them  on database (APPLY MIGRATIONS)
python manage.py migrate

REM invoke python shell 
python manage.py shell