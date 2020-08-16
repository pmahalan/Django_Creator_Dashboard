# Django Creator Dashboard

# Setup / Install

1. git clone https://github.com/pmahalan/Django_Creator_Dashboard.git
2. cd into Django_Creator_Dashboard
3. run the command ```brew install python3```.
4. run the command ```python3 -m venv venv```.
5. run the command ```source venv/bin/activate```.
6. run the command ```python3 manage.py```, to see your options.
7. From that list, run the command ```python3 manage.py runserver```.
8. Open  your browser and visit http://localhost:8000 

# Application

The Django Creator Dashboard is the skeleton of a user dashboard. Its key aspects of functionality are (1) allowing a user to create and subsequently update a public username for themselves, and (2) allowing the user to upload and subsequently update a profile picture for themselves. 

Both these aspects of functionality are effective. When viewing any given user's information from Django Admin, all changes made throughout time can be viewed. 

Moreover, each time a user uploads and submits a new image to use as their profile picture, that image is stored in the 'media' directory, and can be viewed and accessed after having been uploaded through the front-end of the application.

Directions for future development include improving the aesthetic layout of the front-end, and adjusting the formatting so that the profile image (and changes made to it) are visible from the front-end as well as from the 'media' directory of the project's code.
