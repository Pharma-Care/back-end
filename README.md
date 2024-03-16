# Pharma-Care Django REST API back end
<div>This project constitutes the back end functionality of pharma-care project. The front end that uses it can be found <a href='https://github.com/Pharma-Care/front-end'>HERE</a>
</div>

## Installation steps
<div>
clone this repo<br>
<code>git clone https://github.com/Pharma-Care/back-end.git</code><br><br>
go into the project folder<br>
<code>cd back-end</code><br>
<div>
<br>
create a python virtual environment<br>
<code>python3 -m venv env<br>source venv/bin/activate<br>pip install -r requirements.txt</code><br><br>
create the database<br>
<code>python manage.py makemigrations</code> <br><code>python manage.py migrate</code>
</div>
<br>
Finally, Run the server<br>
<code>python manage.py runserver</code>
</div>