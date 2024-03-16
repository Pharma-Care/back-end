# Pharma-Care Django REST API back end
This project constitutes the back end functionality of pharma-care project. The front end that uses it can be found [here]https://github.com/Pharma-Care/front-end

## Installation steps
clone this repo
<code>git clone https://github.com/Pharma-Care/back-end.git</code>
go into the project folder
<code>cd back-end</code>
create a python virtual environment
<code>python3 -m venv env<br>source venv/bin/activate<br>pip install -r requirements.txt</code>
create the database
<code>python manage.py makemigrations<br>python manage.py migrate</code>
Finally, Run the server
<code>python manage.py runserver</code>