# Student_demo
教务管理系统
开发环境：python3 + Django的+ MYSQL
在settings.py文件中进行数据库的更改
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_db',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'',
        'PORT':'3306'
    }
}
首先：使用以下命令生产py文件python manage.py makemigrations
然后在使用python manage.py migrate生成数据库
