from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import R21
import requests
from bs4 import BeautifulSoup
from .scrap import forcesrate, coderate, leetrate, spojrate, get
from concurrent.futures import ThreadPoolExecutor
import itertools

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

    ''' with connection.cursor() as cursor:
        cursor.callproc('get_det')
        results = cursor.fetchall()
        print(results)
    '''


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
    cc_res = {}
    cf_res = {}

    c = 0
    for i in students:
        cc_ids.update({i['codechef_username']: 0})
        cf_ids.update({i['codeforces_username']: 0})
        c = c + 1
        # c IS FOR TESTING PURPOSE ONLY
        if (c > 30):
            break

    cc_res.update(get(cc_ids, coderate))
    cf_res.update(get(cf_ids, forcesrate))

    print(cc_res)
    # for i in students:

    #     roll = i['roll_number']
    #     # print(roll, end="---")
    #     # cc_id = i['codechef_username']
    #     # cf_id = i['codeforces_username']
    #     # spoj_id = i['spoj_username']

    #     # Add multithreading here

    #     cc_prob = coderate(cc_id)
    #     cf_prob = forcesrate(cf_id)
    #     # spoj_prob=spojrate(spoj_id)

    #     stu = R21.objects.get(roll_number=roll)
    #     stu.cc_problems_solved = cc_prob
    #     stu.cf_problems_solved = cf_prob
    #     stu.total_ccps_10_field = cc_prob*10
    #     stu.total_cfps_10_field = cf_prob*10
    #     stu.save()
    context = {
        'updated': 'updated'
    }
    return render(request, 'updating.html', context)
