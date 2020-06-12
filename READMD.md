
# Hierarchical Data and You

A simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. 

## Needed to run:
Poetry shell to read necessary dependencies defined in pyproject.toml and poetry.lock; run "poetry install" to install necessary dependencies. Run "python manage.py runserver" to start a server and see working server in browser.


CHECL - README included in repo that explains the project and anything needed to run it.
	
CHECK - uses django-mptt to create one model: a file object that can be a folder or a "file"
	
CHECK - Uses django-mptt draggable admin to make modifications easy in the admin panel
	
CHECK - Displays the built tree on the homepage
	
3 BONUS POINTS: Add forms to create folders / "files" without using the admin panel.
	
5 BONUS POINTS: Add a basic authentication system where each user has their own tree. Login / logout pages / endpoints included.
	
CHECK - Repo contains pyproject.toml that includes all necessary dependencies to run application
