# To clone and run follow 
* Create an python environment and activate the enviroment 
    > pip install Django==3.2 

    > pip install django-sockpuppet

    > pip install django-sockpuppet[lxml]

    > python manage.py runserver 8010

    > if you are getting error of some sort after running the below and run again 

        sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}

    



# New django project

### Installation 

* Reference
        https://sockpuppet.argpar.se/setup-django

### Procedures
* Create an python environment and activate the enviroment 
    > pip install Django==3.2 

    > pip install django-sockpuppet

    > pip install django-sockpuppet[lxml]

* Create a django project
* Add the following to the setting page
>           INSTALLED_APPS = [
>            'channels',
>            'sockpuppet'
>            ]
* Install
    > python manage.py initial_sockpuppet
        
        In this line every time the npm file tries to save globally the files. There are different approaches to solve this. Reference:https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
        
        My solution to this was from http://npm.github.io/installation-setup-docs/installing/a-note-on-permissions.html
        
> npm config get prefix
        
        I got /usr/local

> sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
        
        Change the permission of the folders specified in the commans

> python manage.py generate_reflex home counter_reflex
        
        This will create the required files necessary 




        


