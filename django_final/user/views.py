import json
import random
import string
from enum import Enum

from django.core import serializers
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.http import require_http_methods

from .models import User, Experiment, ExperimentGrade
max_pop = 0
MAX_INTEREST_LENGTH = 5
loginuser = "coderwang"


#ex_score
@require_http_methods(["GET"])
def ex_score(request):
    response = {}
    try:
        uloginid_input = request.GET.get('uloginid')
        uscore_input = request.GET.get('uscore')
        eid_input = request.GET.get('eid')
        user_db = User.objects.get(uloginid=uloginid_input)
        acutal_uid = user_db.uid
        try:
            experimentgrade_db = ExperimentGrade.objects.get(user_uid=acutal_uid,experiment_eid=eid_input)
            experimentgrade_db.grade = uscore_input
            experimentgrade_db.save()
            response['msg'] = 'exists and success'
            response['error_num'] = 0
            return JsonResponse(response)
        except Exception as e:
            try:
                experimentgrade_db= ExperimentGrade(egid=genRandomString(),experiment_eid=Experiment.objects.get(eid=eid_input),user_uid=user_db,grade=uscore_input)
                experimentgrade_db.save()
                response['msg'] = 'create and success'
                response['error_num'] = 0
                return JsonResponse(response)
            except Exception as e:
                response['msg'] = str(e)
                response['error_num'] = 1
                return JsonResponse(response)
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        return JsonResponse(response)


#car_score
@require_http_methods(["GET"])
def car_score(request):
    response = {}
    try:
        uloginid_input = request.GET.get('uloginid')
        uscore_input = request.GET.get('uscore')
        pwd_input = request.GET.get('pwd')
        user_db = User.objects.get(uloginid=uloginid_input)
        acutal_uid = user_db.uid
        if pwd_input=='1234567':
            response['msg'] = 'pwd right'
        else:
            response['msg'] = 'pwd_error'
            response['error_num']=1
            return JsonResponse(response)
        try:
            experimentgrade_db = ExperimentGrade.objects.get(user_uid=acutal_uid,experiment_eid='1')
            experimentgrade_db.grade = uscore_input
            experimentgrade_db.save()
            response['msg'] = 'exists and success'
            response['error_num'] = 0
            return JsonResponse(response)
        except Exception as e:
            try:
                experimentgrade_db= ExperimentGrade(egid=genRandomString(),experiment_eid=Experiment.objects.get(eid='1'),user_uid=user_db,grade=uscore_input)
                experimentgrade_db.save()
                response['msg'] = 'create and success'
                response['error_num'] = 0
                return JsonResponse(response)
            except Exception as e:
                response['msg'] = str(e)
                response['error_num'] = 1
                return JsonResponse(response)
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        return JsonResponse(response)

#显示实验信息
@require_http_methods(["GET"])
def show_experiment(request):
    response = {}
    

    try:
        eid_input = request.GET.get('eid')
        uloginid_input = request.GET.get('uloginid')
        # experiment_db = Experiment.objects.get(eid=eid_input)
        user_db = User.objects.get(uloginid=uloginid_input)
        uid_1 = user_db.uid
        experimentgrade_db = ExperimentGrade.objects.get(user_uid=uid_1,experiment_eid=eid_input)
        # response['eid'] = experiment_db.eid
        # response['ename'] = experiment_db.ename
        # response['econtent'] = experiment_db.econtent
        response['egrade'] = experimentgrade_db.grade
        response['user'] = 'success'
    except Exception as e:
        response['egrade'] = '您还未参加本实验'
        response['user'] = str(e)

    try:
        eid_input = request.GET.get('eid')
        # uloginid_input = request.GET.get('uloginid')
        experiment_db = Experiment.objects.get(eid=eid_input)
        # user_db = User.objects.get(uloginid=uloginid_input)
        # uid_1 = user_db.uid
        # experimentgrade_db = ExperimentGrade.objects.get(user_uid=uid_1)
        response['eid'] = experiment_db.eid
        response['ename'] = experiment_db.ename
        response['econtent'] = experiment_db.econtent
        # response['egrade'] = experimentgrade_db.grade
        response['experiment'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['experiment'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



#显示用户信息
@require_http_methods(["GET"])
def show_user(request):
    response = {}
    
    try:
        uloginid_input = request.GET.get('uloginid')
        user_db = User.objects.get(uloginid=uloginid_input)
        jname = user_db.jname
        if len(jname) ==0:
            response['jname'] = '尚未绑定jaccount'
            response['ja'] = '尚未绑定jaccount'
            response['name'] = '尚未绑定jaccount'
            response['jnum'] = 1
        else:
            response['jname'] = jname
            response['ja'] = user_db.ja
            response['name'] = user_db.name
            response['jnum'] = 0
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# user注册
@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        # 新建user
        user = User(uid=genRandomString(), uloginid=request.GET.get('uloginid'),
                          upassword=request.GET.get('upassword'))
        user.save()
        # 返回前端response
        response['msg'] = 'success'
        response['error_num'] = 0
    # 处理异常
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 绑定jaccount
@require_http_methods(["GET"])
def bound_jaccount(request):
    response = {}
    uloginid_input = request.GET.get('uloginid')
    uj = request.GET.get('uj')
    try:
        user_1 = User.objects.get(jname=uj)
        response['msg'] = 'jaccount has already been bounded'
        response['error_num'] = 1
    except Exception as e:
        try:
            user_db = User.objects.get(uloginid=uloginid_input)
            # name=request.GET.get('name')
            ja=request.GET.get('ja')
            user_db.jname=uj
            # user_db.name=name
            user_db.ja=ja
            user_db.save()
            # 返回前端response
            response['msg'] = 'success'
            response['error_num'] = 0
        # 处理异常
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
    return JsonResponse(response)


# 修改用户名
@require_http_methods(["GET"])
def edit_loginid(request):
    response = {}
    try:
        newloginid = request.GET.get('newloginid')
        oldloginid = request.GET.get('oldloginid')
        user_db = User.objects.get(uloginid=oldloginid)
        user_db.uloginid=newloginid
        user_db.save()
        # 返回前端response
        response['msg'] = 'success'
        response['error_num'] = 0
    # 处理异常
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 修改密码
@require_http_methods(["GET"])
def edit_password(request):
    response = {}
    try:
        uloginid = request.GET.get('uloginid')
        upassword = request.GET.get('upassword')
        user_db = User.objects.get(uloginid=uloginid)
        user_db.upassword=upassword
        user_db.save()
        # 返回前端response
        response['msg'] = 'success'
        response['error_num'] = 0
    # 处理异常
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# user登录
@require_http_methods(["GET"])
def user_login(request):
    response = {}
    try:
        # 找到user并对比密码
        uloginid_input = request.GET.get('uloginid')
        upassword_input = request.GET.get('upassword')
        upassword_db = User.objects.get(uloginid=uloginid_input)
        if upassword_input == upassword_db.upassword:
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = "password wrong"
            response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)

# jaccount登录
@require_http_methods(["GET"])
def jaccount_login(request):
    response = {}
    uj = request.GET.get('uj')
    uname = request.GET.get('uname')
    try:
        user = User.objects.get(jname=uj)
        # 找到此用户，返回uloginid
        response['uloginid'] = user.uloginid
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        # 数据库中没有此用户，新增用户
        try:
            user = User(uid=genRandomString(), uloginid=uj,
                          upassword=uj, jname=uj, ja = uname)
            user.save()
            response['uloginid'] = uj
            response['msg'] = str(e)
            response['error_num'] = 1
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 2
    return JsonResponse(response)


def genRandomString(slen=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))
