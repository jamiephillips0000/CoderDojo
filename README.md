# CoderDojo

git clone git@github.com:jamiephillips0000/CoderDojo.git

Open a terminal

    pip install Flask


Open FileServer.py and change the line

    pwd = "/home/jamie/git/CODE/PYTHON/FlaskCoderDojo/files/
So that it points to the files directory under the project CoderDojo


Then change directory to the CoderDojo project you just checked out and run the following commands

    export FLASK_APP=FileServer.py
    export FLASK_DEBUG=1
    flask run


Open a browser and look at

    http://127.0.0.1:5000/
