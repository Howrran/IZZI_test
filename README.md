

## Installation

Clone the project to your machine
```bash
git clone https://github.com/Howrran/IZZI_test.git
```
Use the package manager pip to install requirements.

```bash
pip install -r requirements.txt 
```
Change the directory 

```bash
cd izzitest/
```

Run migrations 

```bash
python manage.py migrate
```

Create superuser 

```bash
python manage.py createsuperuser
```

## Usage

Run server
```python
python manage.py runserver
```
### Adding users
For adding new users from csv file go to  
http://127.0.0.1:8000/admin  
Login into your superuser account, then go to   
 http://127.0.0.1:8000/admin/user/user/  
and upload your file

### API

You can reach [API](http://127.0.0.1:8000/api/) by going to  
http://127.0.0.1:8000/api/  
For getting all users go to  
http://127.0.0.1:8000/api/users/  
On that page you can also use filter
