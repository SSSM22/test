from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db import connection, transaction, IntegrityError
from django.db.models import F
from .models import  Averages, StudentMaster, StudentScores
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .scrap import forcesrate, coderate, geeksforgeeks_ranking, interviewbit_ranking, leetrate, spojrate, get,hackerrank_ranking
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import PasswordChangeForm
from  datetime import date
from dotenv import load_dotenv
import numpy as np
load_dotenv()
current_academic_year = 2024

from .announcementform import AnnouncementForm
from .models import Announcement
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

dic_branch = {'hodit': 'it',
              'hodcs': 'cse',
              'hodece': 'ece',
              'hodeee':'eee',
              'hodcsm':'cse(aiml)',
              'hodaid':'aid'
              }


def index(request):
    return render(request, 'index.html')


def admin_panel(request):
    if request.user.is_authenticated:
        form=AnnouncementForm()
        if request.method == 'POST':
            form =AnnouncementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('adminpanel')
        context= {'form':form}
        return render(request, 'admin_panel1.html',context)
    return redirect('/login')

def student_panel(request):
    return render(request, 'student_panel.html')


def hod_panel(request):
    dept=request.session['department']
    # print(len(dept))
    avgs=Averages.objects.values()
    overall_avg = {'cse':[],'it':[],'ece':[],'eee':[],'csm':[],'aids':[],'aiml':[],'mec':[],'civ':[],'college':[]} #dictionary to store the averages of each department
    for i in avgs:
        if i['averages'] != 'dept':
            for j in i:
                if j != 'averages':
                    overall_avg[j].append(float(i[j]))
    # print(overall_avg)

    profiles = StudentMaster.objects.filter(branch=dept)
    # print(profiles)
    profile_details = {"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0}}
    
    year_wise_profiles = {1:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          2:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          3:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          4:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}}  }
    for profile in profiles:
        
        for platform in ['codechef_username', 'codeforces_username', 'spoj_username', 'hackerrank_username', 'interviewbit_username', 'leetcode_username', 'gfg_username']:

            if(getattr(profile,platform) == "None"):
                year_wise_profiles[current_academic_year-profile.year+4][platform]["unregistered"] += 1
            else:
                year_wise_profiles[current_academic_year-profile.year+4][platform]["registered"] += 1

    # print(year_wise_profiles)

    return render(request, 'hod_panel.html', {'hod': request.user.username ,"overall_avg": overall_avg,
                                              'platforms': ['CodeChef', 'CodeForce', 'Geeksforgeeks','Hackerrank','Interviewbit','Leetcode','Spoj'],
                                              'dept':str(dept),
                                              'year_wise_profiles':year_wise_profiles })
def principal_view(request):
    #dept=request.session['department']
    # print(len(dept))
    
    if request.method == 'POST':
        year = request.POST['year']
        students = display_students(request)
        if year == 'all':
            context = {
                'students': students
            }
        else:
            context = {
                'students': students
            }
        return render(request, 'over_view.html', context)
    avgs=Averages.objects.values()
    overall_avg = {'cse':[],'it':[],'ece':[],'eee':[],'csm':[],'aids':[],'aiml':[],'mec':[],'civ':[],'college':[]} #dictionary to store the averages of each department
    for i in avgs:
        if i['averages'] != 'dept':
            for j in i:
                if j != 'averages':
                    overall_avg[j].append(float(i[j]))
    # print(overall_avg)

    profiles = StudentMaster.objects.all()
    # print(profiles)
    profile_details = {"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0}}
    
    year_wise_profiles = {1:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          2:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          3:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}},
                          4:{"codechef_username":{"registered":0,"unregistered":0},"codeforces_username":{"registered":0,"unregistered":0},"gfg_username":{"registered":0,"unregistered":0},"hackerrank_username":{"registered":0,"unregistered":0},"interviewbit_username":{"registered":0,"unregistered":0},"leetcode_username":{"registered":0,"unregistered":0},"spoj_username":{"registered":0,"unregistered":0}}  }
    for profile in profiles:
        
        for platform in ['codechef_username', 'codeforces_username', 'spoj_username', 'hackerrank_username', 'interviewbit_username', 'leetcode_username', 'gfg_username']:

            if(getattr(profile,platform) == "None"):
                year_wise_profiles[current_academic_year-profile.year+4][platform]["unregistered"] += 1
            else:
                year_wise_profiles[current_academic_year-profile.year+4][platform]["registered"] += 1

    # print(year_wise_profiles)

    return render(request, 'principal_view.html', {'principal': request.user.username ,"overall_avg": overall_avg,
                                              'platforms': ['CodeChef', 'CodeForce', 'Geeksforgeeks','Hackerrank','Interviewbit','Leetcode','Spoj'],
                                              
                                              'year_wise_profiles':year_wise_profiles })


def pie_chart(request, roll):
    labels = ['CodeChef', 'CodeForce', 'Geeksforgeeks','Hackerrank','Interviewbit','Leetcode','Spoj']
    data = []
    scores =StudentMaster.objects.select_related('roll_no').get(roll_no=roll)#joining tables studentMaster table has foreign key roll_no
    data.append(scores.roll_no.codechef_score) #accessing the score of codechef of a particular student syntax
    data.append(scores.roll_no.codeforces_score)
    data.append(scores.roll_no.gfg_score)
    data.append(scores.roll_no.hackerrank_score)
    data.append(scores.roll_no.interviewbit_score)
    data.append(scores.roll_no.leetcode_score)
    data.append(scores.roll_no.spoj_score)  
    print(data)
    return (labels, data)


def display_students(request):
    global students
    students = (
    StudentMaster.objects
    .select_related('roll_no')
    .annotate(overall_score=F('roll_no__overall_score'))
    .order_by('-overall_score'))
    return students  
 
def display_students_branch(request,branch):
    global students
    students = (
    StudentMaster.objects
    .select_related('roll_no').filter(branch=branch)
    .annotate(overall_score=F('roll_no__overall_score'))
    .order_by('-overall_score'))
    
    return students 

def validate(request):
    if request.method == 'POST':
        details = request.POST.dict()
        year = details['year']
        branch = details['branch']
        # print(year, branch)
        students = display_students(request)
        if(branch == 'all' and year == 'all'):
            context = {
                'students': students
            }
        elif(branch != 'all' and year != 'all'):
            context = {
            'students': students.filter(branch=branch, year=int(year)+int(current_academic_year))
            }
        elif(year!='all'):
            context = {
            'students': students.filter(year=int(year)+int(current_academic_year))
            }
        else:
            context = {
            'students': students.filter(branch=branch)
            }        
        return render(request, 'over_view.html', context)
    else:
        students = display_students(request)
        s_br=students.filter(roll_no=request.user.username).values_list('branch', flat=True)[0] #getting the branch of the student from queryset
        return render(request, 'over_view.html', {'students': students.filter(branch=s_br)})

@login_required
def report(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    score_gt = request.GET.get('score_gt', '')  # Score greater than
    score_lt = request.GET.get('score_lt', '')
    students = display_students(request)
    if q:
        students = students.filter(branch=q)
    if score_gt:
        students = students.filter(overall_score__gt=float(score_gt))
    if score_lt:
        students = students.filter(overall_score__lt=float(score_lt))
    distinct_branches = StudentMaster.objects.values_list('branch', flat=True).distinct()
    context = {
        'students': students,
        'branches': distinct_branches
    }
    if(request.user.is_staff and (not request.user.is_superuser)):
        context['branch'] = dic_branch[request.user.username]
    return render(request, 'report.html', context)

@login_required
def load_rows(request):
    checks = request.GET.get("checks")
    print(checks)
    if(checks != None):
        students = display_students_branch(request,checks)
        return render(request,"report_rows.html",{"students":students})
    students = display_students(request)
    return render(request,"report_rows.html",{"students":students})
    
    # table_body = request.GET.get("table_body")
    # if(request.user.is_staff == True ):
    #     students = StudentMaster.objects.select_related('roll_no').annotate(overall_score=F('roll_no__overall_score')).order_by('-overall_score').filter(branch=dic_branch[request.user.username])

def update(request):
    student = StudentMaster.objects.all().values() #getting all the students from the database
    c = 0
    cc_data=[]
    cf_data=[]  
    sp_data=[]
    ib_data=[]
    lc_data=[]
    gfg_data=[]
    hackerrank_data=[]
    for i in student: #iterating through the students list and adding them to the usernames dictionary
        #roll_no_id is used because the roll_no is a foreign key in StudentScores table
        cc_data.append({"roll_no":i['roll_no_id'],'id':i['codechef_username'],'score':0})
        cf_data.append({"roll_no":i['roll_no_id'],'id':i['codeforces_username'],'score':0})
        sp_data.append({"roll_no":i['roll_no_id'],'id':i['spoj_username'],'score':0})
        ib_data.append({"roll_no":i['roll_no_id'],'id':i['interviewbit_username'],'score':0})
        lc_data.append({"roll_no":i['roll_no_id'],'id':i['leetcode_username'],'score':0})
        gfg_data.append({"roll_no":i['roll_no_id'],'id':i['gfg_username'],'score':0})
        hackerrank_data.append({"roll_no":i['roll_no_id'],'id':i['hackerrank_username'],'score':0})

    # cc_data = get(cc_data, coderate)
    # cf_data = get(cf_data, forcesrate)
    # sp_data = get(sp_data, spojrate)
    # gfg_data = get(gfg_data, geeksforgeeks_ranking)
    lc_data = get(lc_data, leetrate)
    print(lc_data)
    # ib_data = get(ib_data, interviewbit_ranking) # Looks like students didnt provide the right usernames for interviewbit
    # hackerrank_data = get(hackerrank_data, hackerrank_ranking)
    
    # print(sp_res,gfg_res,lc_res,ib_res)
    # print(cc_data)
    # # try:
    #     with transaction.atomic():
    #         # for i in cc_data: #roll_no_id is used because the roll_no is a foreign key in StudentScores table
    #         #     # try:
    #         #     #     student_score = StudentScores.objects.get(roll_no=i['roll_no'])
    #         #     #     student_score.codechef = i['score']
    #         #     #     student_score.save()
    #         #     # except ObjectDoesNotExist:
    #         #         # print(f"Student with roll_no {i['roll_no']} does not exist.")

    #         #     ans = str(StudentScores.objects.get(roll_no=i['roll_no']).codechef) + ',' + str(i['score'])
    #         #     points = i['score'] * 10

    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         codechef=ans)
    #         #     # print(points)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         codechef_score=points)
    #         # for i in cf_data:
    #         #     # try:
    #         #     #     student_score = StudentScores.objects.get(roll_no=i['roll_no'])
    #         #     #     student_score.codeforces = i['score']
    #         #     #     student_score.save()    
    #         #     # except ObjectDoesNotExist:
    #         #     #     print(f"Student with roll_no {i['roll_no']} does not exist.")   
    #         #     ans=str(StudentScores.objects.get(roll_no=i['roll_no']).codeforces)+','+str(i['score'])
    #         #     points=i['score']*10
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         codeforces=ans)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         codeforces_score=points)
    #         # for i in sp_data:
    #             # try:
    #             #     student_score = StudentScores.objects.get(roll_no=i['roll_no'])
    #             #     student_score.spoj = i['score']
    #             #     student_score.save()
    #             # except ObjectDoesNotExist:
    #             #     print(f"Student with roll_no {i['roll_no']} does not exist.")
    #             # ans=str(StudentScores.objects.get(roll_no=i['roll_no']).spoj)+','+str(i['score'])
    #             # points=i['score']*20
    #             # StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #             #     spoj=ans)
    #             # StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #             #     spoj_score=points)
    #         # for i in gfg_data:
    #         #     ans=str(StudentScores.objects.get(roll_no=i['roll_no']).gfg)+','+str(i['score'])
    #         #     points=i['score']
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         gfg=ans)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         gfg_score=points)        
    #         # for i in lc_data:
    #         #     ans=str(StudentScores.objects.get(roll_no=i['roll_no']).leetcode)+','+str(i['score'])
    #         #     points=i['score']*50
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         leetcode=ans)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         leetcode_score=points)
    #         # for i in ib_data:
    #         #     ans=str(StudentScores.objects.get(roll_no=i['roll_no']).interviewbit)+','+str(i['score']//3)
    #         #     points=i['score']//3
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         interviewbit=ans)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         interviewbit_score=points)    
    #         # for i in hackerrank_data:
    #         #     ans=str(StudentScores.objects.get(roll_no=i['roll_no']).hackerrank)+','+str(i['score'])
    #         #     points=i['score']
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #         #         hackerrank=ans)
    #         #     StudentScores.objects.filter(roll_no=i['roll_no']).update(
    #                 hackerrank_score=points) 
    #     print("db updated")               
    #     with connection.cursor() as cursor:
    #         cursor.callproc('new_procedure')
    #     #     cursor.callproc('update_rank')
    #         cursor.close()

    # except IntegrityError:
    #     return HttpResponse("DB ERROR")

    return HttpResponse("updated")


def auth_login(request):
    if request.GET.get('next'):
        messages.add_message(request, messages.WARNING,
                             "Please login before proceeding")

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            group = ""
            if len(user.groups.all()):
                group = str(user.groups.all()[0])
            print(group)
            login(request, user)
            
            if group=="hods":
                request.session['department']=dic_branch[username] #storing department of the HOD logged in, to 
                return redirect('/hod_panel')
            if group=="principal":
                return redirect('/principal_view')
            if user.is_superuser:
                return redirect("/admin_panel")
            else:
                st=StudentMaster.objects.get(roll_no=username)
                if user.last_login is None: #if user is logging in for the first time then he will be redirected to change password page
                    login(request, user)   
                    return redirect('/change_password')
                if(st.hackerrank_username=='None' or st.codechef_username=='None' or st.codeforces_username=='None' or st.spoj_username=='None' or st.interviewbit_username=='None' or st.leetcode_username=='None' or st.gfg_username=='None'):
                    messages.info(request, 'Please fill in all your usernames and login again to view your profile')
                    return redirect('/usernames')
            
                return redirect('/student_view/'+username)

        else:
            messages.warning(request, 'Enter correct credentials')
            return redirect("/login")
    return render(request, 'login.html')

@login_required
def student_view(request, username):
    if(request.user.is_authenticated):
        if(request.user.is_staff and username is not None):
            roll = username
        else:
            roll = request.user.username
        announcement = Announcement.objects.all()
        # scatter_plot(request,roll)
        det = StudentMaster.objects.select_related('roll_no').filter(roll_no=roll)
        print(det[0].branch)
        labels, data = pie_chart(request, roll)
        # below code for graph below is the samlpe data
        data_string = "10,20,30,40,52,68,78,80,90,100,100,100,100,110,115,125,130,140,150,150,150,190,200,210,211,215,215,215,220,220";
        Gdata = [int(x.strip()) for x in data_string.split(',')]
        Glabels = [str(i+1) for i in range(30)]
        #end graph
        average_scores={"dept":[], "college":[]}
        # codechef_average = StudentScores.objects.values_list('codechef_score')

        avgs = Averages.objects.values()
        for i in avgs:
            if i['averages'] != 'dept':
                for j in i:
                    if j == det[0].branch:
                        average_scores["dept"].append(float(i[j]))
                    if j == "college":
                        average_scores["college"].append(float(i[j]))
            
        context = {
            'staff': request.user.is_staff,
            'username': roll,
            'det': det,
            'labels': labels,
            'data': data,
            'students': det,
            'image':det.values_list('branch')[0][0],#getting the branch of the student from queryset
            'announcements': announcement,
            'Glabels': Glabels,
            'Gdata': Gdata,
            'platforms': ['CodeChef', 'CodeForce', 'Geeksforgeeks','Hackerrank','Interviewbit','Leetcode','Spoj'],
            'average_scores':average_scores,

        }
        return render(request, 'student_panel.html', context)
    
    return redirect('/login')
@login_required
def hod_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        students = display_students(request)
        if request.method == 'GET':
            roll = request.GET["Roll"]
            students = display_students(request)
            students = students.filter(roll_no=roll)
            request.session['search_roll'] = roll #saving into session variable to access it in the next view
            if(students.count()==0):
                messages.info(request, 'No students found')
                return redirect('hod')
            context = {
                'students': students
            }
            # return render(request, 'report.html', context)
            return redirect('student_view/'+roll)
        if request.method == 'POST':
            year = request.POST['year']
            students = display_students(request)
            if year == 'all':
                if username == 'vceprincipal':
                    context = {
                        'students': students
                    }
                else:
                    context = {
                        'students': students.filter(branch=dic_branch[username])
                    }   
            else:
                if username == 'vceprincipal':
                    context = {
                        'students': students.filter(year=int(year)+int(current_academic_year))
                    }
                else:    
                    context = {
                        'students': students.filter(year=int(year)+int(current_academic_year),branch=dic_branch[username])
                    }
            return render(request, 'over_view.html', context)
    return redirect('/login')

def auth_logout(request):
    logout(request)
    print("logged out")
    return redirect("/login")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.info(
                request, 'Your password has been changed successfully!')
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('/logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@login_required
def usernames(request):
    if(request.user.is_staff):
        roll =request.session['search_roll']
        print(roll)
    else:
        roll = request.user.username
    un = StudentMaster.objects.all().filter(roll_no=roll)
    context = {
        'un': un     
    }
    return render(request, 'usernames.html', context)

@login_required
def update_usernames(request):
    if request.method == 'POST':
        hu = request.POST['hackerrank_username']
        cf = request.POST['codeforces_username']
        cc = request.POST['codechef_username']
        sp = request.POST['spoj_username']
        ib = request.POST['interviewbit_username']
        lc = request.POST['leetcode_username']
        gfg = request.POST['gfg_username']
        if(request.user.is_staff):
            roll =request.session['search_roll']
            print(roll)
        else:
                roll = request.user.username  # change this when student doesnt require editing usernames
        StudentMaster.objects.filter(roll_no=roll).update(hackerrank_username=hu, codeforces_username=cf,codechef_username=cc, spoj_username=sp, interviewbit_username=ib, leetcode_username=lc, gfg_username=gfg)
        messages.success(request, "Sucessfully Upated")

    return redirect('/usernames')


@login_required(login_url='/login')
def profile(request):
    # username = None
    # if request.user.is_authenticated:
    #     username = request.user.username
    #     students = display_students(request, 3, "IT")
    return render(request, "random.html", {'platforms': ['CodeChef', 'CodeForce', 'Spoj','Hackerrank','Interviewbit','Leetcode','Geeksforgeeks'],
                                           'average_score_data':[100,200,300,400,500,600,700],
                                           'student_score_data': [50,100,150,200,250,300,350]})
