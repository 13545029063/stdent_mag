from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    sex=models.CharField(max_length=1)
    students_cls = models.ForeignKey('Cls_student', on_delete=models.CASCADE)
    # 班级和学生是1对多
class teachers(models.Model):
    name=models.CharField(max_length=20)
    #老师姓名
    coanhing_years=models.IntegerField()
    #执教年限
    Entry_time=models.DateField()
    #入职日期
    thear_student=models.ManyToManyField("students")
    #老师和学生形成多对多的关系
class course_1(models.Model):
    course=models.CharField(max_length=20)
    #课程名
    course_stu =models.ManyToManyField('students')
    # 学生和课程形成1对多的关系
    #course_t=models.ForeignKey('teachers',on_delete=models.CASCADE)
class Cls_student(models.Model):
    CLS_name=models.CharField(max_length=6)
    cls_thear=models.ManyToManyField("teachers")
    #班级和老师形成多对多的关系
