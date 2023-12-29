from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db import connection, transaction, IntegrityError
from django.db.models import F
from .models import R21, R22, StudentMaster, StudentScores
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .scrap import forcesrate, coderate, geeksforgeeks_ranking, interviewbit_ranking, leetrate, spojrate, get,hackerrank_ranking
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
# from .forms import UsernamesForm
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from django.urls import reverse_lazy
# from django.contrib.auth.views import PasswordResetView
# from django.contrib.messages.views import SuccessMessageMixin
from  datetime import date

# Create your views here.

dic_branch = {'hodit': 'it',
              'hodcs': 'cse',
              'hodece': 'ece',
              'hodeee':'eee'

              }
scraped_dates=['December 25, 2023','December 26, 2023']


def index(request):
    return render(request, 'index.html')


def admin_panel(request):
    return render(request, 'admin_panel1.html')


def student_panel(request):
    return render(request, 'student_panel.html')


def hod_panel(request):
    return render(request, 'hod_panel.html', {'hod': request.user.username})


def scatter_plot(request,roll):
    # Assuming you have obtained x_values and y_values in your view
    y_values =list(map(int,StudentScores.objects.all().get(roll_no=roll).daily_scores.split(',')))
    return(scraped_dates, y_values)

def pie_chart(request, roll):
    labels = ['CodeChef', 'CodeForce', 'Spoj','Hackerrank','Interviewbit','Leetcode','Geeksforgeeks']
    data = []
    scores =StudentMaster.objects.select_related('roll_no').get(roll_no=roll)#joining tables studentMaster table has foreign key roll_no
    data.append(scores.roll_no.codechef_score) #accessing the score of codechef of a particular student syntax
    data.append(scores.roll_no.codeforces_score)
    data.append(scores.roll_no.spoj_score)
    data.append(scores.roll_no.hackerrank_score)
    data.append(scores.roll_no.interviewbit_score)
    data.append(scores.roll_no.leetcode_score)
    data.append(scores.roll_no.gfg_score)
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

def validate(request):
    if request.method == 'POST':
        details = request.POST.dict()
        year = int(details['year'])
        branch = details['branch']
        print(year, branch)

        students = display_students(request)

        context = {
            'students': students.filter(branch=branch, year=year)

        }
        return render(request, 'over_view.html', context)
    else:
        students = display_students(request)
        return render(request, 'over_view.html', {'students': students})


def report(request):
    students = display_students(request)
    context = {
        'students': students

    }
    return render(request, 'report.html', context)


def update(request):
    scraped_dates.append(date.today().strftime("%B %d, %Y"))
    student = StudentMaster.objects.all().values()
    c = 0
    cc_data=[]
    cf_data=[]  
    sp_data=[]
    ib_data=[]
    lc_data=[]
    gfg_data=[]
    hackerrank_data=[]
    for i in student: 
        #roll_no_id is used because the roll_no is a foreign key in StudentScores table
        cc_data.append({"roll_no":i['roll_no_id'],'id':i['codechef_username'],'score':0})
        cf_data.append({"roll_no":i['roll_no_id'],'id':i['codeforces_username'],'score':0})
        sp_data.append({"roll_no":i['roll_no_id'],'id':i['spoj_username'],'score':0})
        ib_data.append({"roll_no":i['roll_no_id'],'id':i['interviewbit_username'],'score':0})
        lc_data.append({"roll_no":i['roll_no_id'],'id':i['leetcode_username'],'score':0})
        gfg_data.append({"roll_no":i['roll_no_id'],'id':i['gfg_username'],'score':0})
        hackerrank_data.append({"roll_no":i['roll_no_id'],'id':i['hackerrank_username'],'score':0})

    #     c = c + 1
    #    # c IS FOR TESTING PURPOSE ONLY
    #     if (c > 30):
    #         break

    cc_data = get(cc_data, coderate)
    cf_data = get(cf_data, forcesrate)
    sp_data = get(sp_data, spojrate)
    gfg_data = get(gfg_data, geeksforgeeks_ranking)
    lc_data = get(lc_data, leetrate)
    ib_data = get(ib_data, interviewbit_ranking) # Looks like students didnt provide the right usernames for interviewbit
    hackerrank_data = get(hackerrank_data, hackerrank_ranking)
    
    # print(sp_res,gfg_res,lc_res,ib_res)
    print(cc_data)
    try:
        with transaction.atomic():
            for i in cc_data: #roll_no_id is used because the roll_no is a foreign key in StudentScores table
                ans=str(StudentScores.objects.get(roll_no=i['roll_no_id']).codechef)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no_id']).codechef_score+i['score']*10
                StudentScores.objects.filter(roll_no=i['roll_no_id']).update(
                    codechef=ans)
                StudentScores.objects.filter(roll_no=i['roll_no_id']).update(
                    codechef_score=points)
            for i in cf_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no_id']).codeforces)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no_id']).codeforces_score+i['score']*10
                StudentScores.objects.filter(roll_no=i['roll_no_id']).update(
                    codeforces=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    codeforces_score=points)
            for i in sp_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no']).spoj)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no']).spoj_score+i['score']*20
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    spoj=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    spoj_score=points)
            for i in gfg_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no']).gfg)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no']).gfg_score+i['score']
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    gfg=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    gfg_score=points)        
            for i in lc_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no']).leetcode)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no']).leetcode_score+i['score']*50
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    leetcode=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    leetcode_score=points)
            for i in ib_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no']).interviewbit)+','+str(i['score']//3)
                points=StudentScores.objects.get(roll_no=i['roll_no']).interviewbit_score+i['score']//3
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    interviewbit=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    interviewbit_score=points)    
            for i in hackerrank_data:
                ans=str(StudentScores.objects.get(roll_no=i['roll_no']).hackerrank)+','+str(i['score'])
                points=StudentScores.objects.get(roll_no=i['roll_no']).hackerrank_score+i['score']
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    hackerrank=ans)
                StudentScores.objects.filter(roll_no=i['roll_no']).update(
                    hackerrank_score=points)    
        with connection.cursor() as cursor:
            cursor.callproc('overall_score')
        #     cursor.callproc('update_rank')
        #     cursor.close()

    except IntegrityError:
        return HttpResponse("DB ERROR")

    return HttpResponse("updated")


def auth_login(request):
    if request.GET.get('next'):
        messages.add_message(request, messages.WARNING,
                             "Please login before proceeding")

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            if user.is_superuser:
                return redirect("/admin_panel")
            if user.is_staff:
                return redirect('/hod_panel')
            st=StudentMaster.objects.get(roll_no=username)
            if(st.hackerrank_username=='None' or st.codechef_username=='None' or st.codeforces_username=='None' or st.spoj_username=='None' or st.interviewbit_username=='None' or st.leetcode_username=='None' or st.gfg_username=='None'):
                messages.info(request, 'Please fill in all your usernames and login again to view your profile')
                return redirect('/usernames')
            return redirect('/student_view/'+username)

        else:
            return HttpResponse("Enter correct credentials")
    return render(request, 'login.html')


def student_view(request, username):
    roll = request.user.username
    # scatter_plot(request,roll)
    det = StudentMaster.objects.select_related('roll_no').filter(roll_no=roll)
    print(det)
    labels, data = pie_chart(request, roll)
    xvalues, yvalues =scatter_plot(request,roll)
    print(xvalues,yvalues)
    context = {
        'username': roll,
        'det': det,
        'labels': labels,
        'data': data,
        'students': det,
        'xValues':xvalues,
        'yValues':yvalues,
        'image':det.values_list('branch')[0][0]#getting the branch of the student from queryset
    }
    return render(request, 'student_panel.html', context)


def hod_view(request):
    username = request.user.username

    if request.method == 'GET':
        roll = request.GET["Roll"]
        students = display_students(request,)

        students = students.filter(roll_no=roll)
        if(students.count()==0):
            messages.info(request, 'No students found')
            return redirect('hod')
        context = {
            'students': students
        }
        return render(request, 'report.html', context)

    if request.method == 'POST':
        year = request.POST['year']
        students = display_students(request,)
        context = {
            'students': students.filter(year=year,branch=dic_branch[username])

        }
        return render(request, 'over_view.html', context)


def auth_logout(request):
    logout(request)
    return redirect("/login")


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


# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'password_reset.html'
#     email_template_name = 'password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('login')

# views.py

@login_required
def usernames(request):
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
        StudentMaster.objects.filter(roll_no=request.user.username).update(hackerrank_username=hu, codeforces_username=cf,
                                                                           codechef_username=cc, spoj_username=sp, interviewbit_username=ib, leetcode_username=lc, gfg_username=gfg)
        messages.success(request, "Sucessfully Upated")

    return redirect('/usernames')


@login_required(login_url='/login')
def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        students = display_students(request, 3, "IT")
    return render(request, "student_panel.html", {'username': username})
