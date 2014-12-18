lou
===

Computational Hydrology


Welcome to LOU.

This is an initial attempt to migrate a matlab code developed by professor Christopher Souza (UFAL) to Python.

The migration is coordinated by professor Rodrigo Paes (UFAL)


# Tutorial

*   Install Python: [https://www.python.org/download/](https://www.python.org/download/)
    *   Put Python in the PATH
*   Install PIP: [https://pypi.python.org/pypi/pip](https://pypi.python.org/pypi/pip)
    *   It will be installed under the Script directory in your Python installation folder. Put this Script directory in your PATH
*   Install Django
    *   Open the command prompt and type: `pip install Django==1.7.1`

*   pip install djangorestframework
*   pip install markdown       # Markdown support for the browsable API.
*   pip install django-filter

*   Create a github account: [https://github.com/](https://github.com/)
*   Install git: [http://git-scm.com/downloads](http://git-scm.com/downloads)
*   Install a github client for windows: [https://windows.github.com/](https://windows.github.com/)
*   Create a fork of the github project: [https://github.com/r0drigopaes/lou/fork](https://github.com/r0drigopaes/lou/fork)
*   Go to your local directory where you download the source files and open a command prompt
    *   Type: `python manage.py test` For example: `D:\symform\desenv\lou>python manage.py test`
    *   All tests should run. The output should look like:


       `
       Creating test database for alias 'default'...
       ...
        ----------------------------------------------------------------------
        Ran 3 tests in 0.256s
        OK
        Destroying test database for alias 'default'...
        `
* You are ready to go. Just type: `python manage runserver` to run the server. Now, open your browser and type: [http://localhost:8000/cohy](http://localhost:8000/cohy) to access the application




