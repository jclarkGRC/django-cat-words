# Category Words Game

This is a simple yet fun word game.  The idea is to guess as many words as you can to the related topic chosen at the beginning of the game.  The trick is you only have 30 seconds for each guess.  If you can't guess any more words your time is up! Good Luck!

## How to use the application

The application is written using the Django framework.

Set up your database configuration in the settings.py within the mysite directory.  More information on setting up databases with Django is available here: https://docs.djangoproject.com/en/2.2/topics/install/#database-installation

After setting up your database run the following command:

python manage.py runserver

This will start a development server with the Cat Words application running on http://localhost:8000/game.

You can view the admin dashboard for the application by navigating to http://localhost:8000/admin.  There you can manage the database with the UI admin interface without having to use the Python Shell.

## How was the application built?

This application was based on following the first application tutorial on Djangos website.  That tutorial is available here: https://docs.djangoproject.com/en/2.2/intro/tutorial01/. After that I expanded and learned as I went while adding new features and concepts.

Enjoy the game!