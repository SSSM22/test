from django.shortcuts import render, HttpResponse
from django.db import connection,transaction,IntegrityError
from .models import R21
import requests
from bs4 import BeautifulSoup
from .scrap import forcesrate, coderate, leetrate, spojrate,get

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_students(request, year, br):

    if (year == '3rd'):
        if (br != 'all'):
            students = R21.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R21.objects.all().order_by('-overall_score')
    if (year == '2nd'):
        if (br != 'all'):
            students = R22.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R22.objects.all().order_by('-overall_score')
    if (year == '1st'):
        if (br != 'all'):
            students = R23.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R23.objects.all().order_by('-overall_score')

    if (year == '4th'):
        if (br != 'all'):
            students = R20.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R20.objects.all().order_by('-overall_score')

    return students
    # return render(request,'display.html',context)

 
    


def validate(request):
    if request.method == 'POST':
        details = request.POST.dict()
        year = details['year']
        branch = details['branch']
        print(year, branch)

        students = display_students(request, year, branch)
        context = {
            'students': students
            
        }
        return render(request, 'display.html', context)


def update(request):

    students = R21.objects.all().values()

    cc_ids = {}
    cf_ids = {}
    sp_ids={}
    cc_res = {}
    cf_res = {}
    sp_res={}
    c = 0
    for i in students:
        cc_ids.update({i['codechef_username']: 0})
        cf_ids.update({i['codeforces_username']: 0})
        sp_ids.update({i['spoj_username']: 0})

        c = c + 1
        # c IS FOR TESTING PURPOSE ONLY
        # if (c > 30):
        #     break

    cc_res.update(get(cc_ids, coderate))
    cf_res.update(get(cf_ids, forcesrate))
    sp_res.update(get(sp_ids, spojrate))

    print(sp_res)
    
    try:
        with transaction.atomic():
            for key, value in cc_res.items():
                R21.objects.filter(codechef_username=key).update(cc_problems_solved=value)
                R21.objects.filter(codechef_username=key).update(ccps_10=value*10)
            for key,value in cf_res.items():
                 R21.objects.filter(codeforces_username=key).update(cf_problems_solved=value)
                 R21.objects.filter(codeforces_username=key).update(cfps_10=value*10)
            for key,value in sp_res.items():
                R21.objects.filter(codeforces_username=key).update(cf_problems_solved=value)
                R21.objects.filter(codeforces_username=key).update(cfps_10=value*10)
            
        with connection.cursor() as cursor:
            cursor.callproc('update_overall_score')
            cursor.callproc('update_rank')
            cursor.close()             

    except IntegrityError:
        return HttpResponse("DB ERROR")
    

    return HttpResponse("updated")
    
