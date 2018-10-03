from django.shortcuts import render,HttpResponse,redirect
from Student_sys1.models import *
# Create your views here.
UserList=[]
itme=range(0,99)
for i in itme:
    index_ment={"naem":"root"+str(i),"age":i}
    UserList.append(i)
def manypage(request):
    page_get=request.GET.get('p')
    page_get_int=(int(page_get)-1)*10
    end_page = int(page_get)*10
    UserList_page=UserList[page_get_int:end_page]
    return render(request,'21.html',{"userList":UserList_page})
def index(request):

    return render(request, 'register.html')
def students_Html(request):

    return render(request,'student.html')


def select_stu(request):#查找功能
    stu=students.objects.all().values('id','name','sex','age','teachers__name','students_cls__CLS_name')
    return render(request,"student.html",{'stu':stu})
def addStudent(request):#添加功能
    Name=request.POST.get('Name')
    age=request.POST.get('age')
    sex=request.POST.get('sex')
    Cls=request.POST.get('Cls')
    tea = request.POST.get('teacher')#以上五个接受前端提交的数据
    if sex=='0':
        sex='男'
    else:#对性别进行判断0 是男 1是女
        sex='女'
    CLS_stu= Cls_student.objects.filter(CLS_name=Cls).values('id')[0]['id']#获取前端传回班级信息的ID
    teacher = teachers.objects.filter(name=tea).values('id')[0]['id']#获取前端传回的老师ID
    student=students.objects.create(name=Name,age=age,sex=sex,students_cls_id=CLS_stu)#为数据库添加学生信息，和班级外键
    student_tea = students.objects.filter(name=Name).first()#表关联查询，返回JQUERY SET对象
    student_tea.teachers_set.add(teacher)#对学生和老师进行关联
    return HttpResponse('ok')

def writ_content(request):#编辑功能未完成
    nid = request.POST.get('nid')
    name1= request.POST.get('name')
    age1 = request.POST.get('age')
    sex1 = request.POST.get('sex')
    Cls1 = request.POST.get('Cls')
    theacher1 = request.POST.get('theacher')
    if sex1=='0':
        sex1='男'
    else:#对性别进行判断0 是男 1是女
        sex1='女'
    room_id= Cls_student.objects.filter(CLS_name=Cls1).values('id')[0]['id']
    stu = students.objects.filter(id=nid).update(name=name1, sex=sex1, age=age1,students_cls_id=room_id)#已修改学生表中的信息，外键信息还未修改
    tea_id = teachers.objects.filter(name=theacher1).values('id')[0]['id']
    stu2=students.objects.filter(name=name1).first()
    stu2.teachers_set.set([tea_id])
    return HttpResponse('1')
def delete_allline(request):#删除功能
    nid=request.POST.get('nid')
    students.objects.filter(id=nid).delete()
    print('触发成功')
    return HttpResponse('删除成功')