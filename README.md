# Student_demo
基于PC端教务管理系统  
开发环境：python3 + Django的+ MYSQL+bootstrap  
在settings.py文件中进行数据库的更改  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'student_db',#数据库名称在生产数据库表时需要先建立一个数据库。   
        'USER':'root',  
        'PASSWORD':'root',  
        'HOST':'',  #默认为本机
        'PORT':'3306'  
    }  
}  


首先：使用以下命令生产py文件python manage.py makemigrations  
其次：在使用python manage.py migrate生成数据库
最后：通过python manage.py runserver 8080命令运行

主要功能有：添加学生信息   
删除学生信息   
学生信息查询     
修改学生信息   
后台采用的是Django自带的admin进行数据库的管理

