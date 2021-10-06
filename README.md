# Goods-platform
Django 3.x  w/ Postgresql

### 사용 절차
   
```bash
1. git clone https://github.com/gwangjinjeong/Goods-platform.git 
2. cd Goods-platform    
3. pip install virtualenv    
4. virtualenv venv    
5. source venv/bin/activate    
6. pip install -r requirements.txt    
7. sudo apt-get install update && sudo apt-get install upgrade      
8. sudo apt-get install postgresql postgresql-contrib       
9. sudo service postgresql restart    
10. sudo -u postgres psql    
11. CREATE DATABASE fanarcade_db;    
12. ALTER user postgres with password '1100';   
13. ALTER role postgres set client_encoding to 'utf-8';       
14. ALTER role postgres set timezone to 'Asia/Seoul';   
15. \q    
16. python manage.py makemigrations    
17. python manage.py migrate    
18. python manage.py createsuperuser    
19. python manage.py runserver 0:80    
20. GO TO [WEBPAGE]/admin    
```   

### API 의 EndPoint

### [ rest-auth ]

- /auth/login/ (POST)
    - username
    - email
    - password

    Returns Token key

- /auth/logout/ (POST)
- /auth/password/reset/ (POST)
    - email
- /auth/password/reset/confirm/ (POST)
    - uid
    - token
    - new_password1
    - new_password2
- /auth/password/change/ (POST)
    - new_password1
    - new_password2
    - old_password
- /auth/user/ (GET, PUT, PATCH)
    - username
    - first_name
    - last_name

    Returns pk, username, email, first_name, last_name

### [ registration ]

- /rest-auth/registration/ (POST)
    - username
    - password1
    - password2
    - email
- /rest-auth/registration/verify-email/ (POST)
    - key


---   

![프로그램 정의서](https://user-images.githubusercontent.com/58495252/136119763-a8e199b2-22ff-4833-a266-ec423bcac5d0.jpg)
