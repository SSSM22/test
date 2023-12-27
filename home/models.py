from django.db import models

# Create your models here.
class R21(models.Model):
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    roll_number = models.CharField(db_column='Roll_Number', primary_key=True, max_length=12)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=39, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateField(db_column='LAST_LOGIN', blank=True, null=True)  # Field name made lowercase.
    mobile = models.BigIntegerField(db_column='Mobile')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    algorithms_hackerrank_field = models.CharField(db_column='Algorithms', max_length=16)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    codechef_username = models.CharField(db_column='CodeChef_UserName', max_length=19)  # Field name made lowercase.
    cc_problems_solved = models.IntegerField(db_column='CC_Problems_Solved')  # Field name made lowercase.
    ccps_10 = models.IntegerField(db_column='CCPS_10',default=0)  # Field name made lowercase.
    codeforces_username = models.CharField(db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cf_problems_solved = models.IntegerField(db_column='CF_Problems_Solved')  # Field name made lowercase.
    cfps_10 = models.IntegerField(db_column='CFPS_10',default=0)  # Field name made lowercase.
    spoj_username = models.CharField(db_column='Spoj_UserName', max_length=19, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    spoj_problems_solved = models.IntegerField(db_column='Spoj_Problems_Solved')  # Field name made lowercase.
    sps_20 = models.IntegerField(db_column='SPS_20',default=0)  # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_Score')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'r21'


class R22(models.Model):
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=31, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=54, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    roll_number = models.CharField(db_column='Roll_Number', primary_key=True, max_length=11)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='Mobile_No', max_length=11, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_UserName', max_length=26, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    algorithms = models.IntegerField(db_column='Algorithms', blank=True, null=True)  # Field name made lowercase.
    codeforces_username = models.CharField(db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cf_problems_solved = models.IntegerField(db_column='CF_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    cfps_10 = models.IntegerField(db_column='CFPS_10', blank=True, null=True)  # Field name made lowercase.
    codechef_username = models.CharField(db_column='CodeChef_UserName', max_length=19, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cc_problems_solved = models.IntegerField(db_column='CC_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    ccps_10 = models.IntegerField(db_column='CCPS_10', blank=True, null=True)  # Field name made lowercase.
    spoj_username = models.CharField(db_column='Spoj_UserName', max_length=18, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    spoj_problems_solved = models.IntegerField(db_column='Spoj_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    sps_20 = models.IntegerField(db_column='SPS_20', blank=True, null=True)  # Field name made lowercase.
    interviewbit_username = models.CharField(db_column='InterviewBit_Username', max_length=37, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    ib_problems_solved = models.IntegerField(db_column='IB_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    ib_10 = models.IntegerField(db_column='IB_10', blank=True, null=True)  # Field name made lowercase.
    leetcode_username = models.CharField(db_column='LeetCode_Username', max_length=23, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    leet_problems_solved = models.IntegerField(db_column='Leet_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    lp_10 = models.IntegerField(db_column='LP_10', blank=True, null=True)  # Field name made lowercase.
    geeksforgeeks_username = models.CharField(db_column='GeeksForGeeks_Username', max_length=24, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    gfg_problems_solved = models.IntegerField(db_column='GFG_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    gfg_10 = models.IntegerField(db_column='GFG_10', blank=True, null=True)  # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_Score')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'r22'

class StudentMaster(models.Model):
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    roll_no = models.OneToOneField('StudentScores', models.DO_NOTHING, db_column='ROLL_NO', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=39)  # Field name made lowercase.
    course = models.CharField(db_column='Course', max_length=7, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=3, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    sec = models.CharField(db_column='Sec', max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_Username', max_length=48, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    codeforces_username = models.CharField(db_column='CodeForces_Username', max_length=40, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    codechef_username = models.CharField(db_column='CodeChef_Username', max_length=92, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    spoj_username = models.CharField(db_column='Spoj_Username', max_length=22, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    interviewbit_username = models.CharField(db_column='InterviewBit_Username', max_length=42, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    leetcode_username = models.CharField(db_column='LeetCode_Username', max_length=29, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    gfg_username = models.CharField(db_column='GFG_Username', max_length=48, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_master'


class StudentScores(models.Model):
    roll_no = models.CharField(db_column='ROLL_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    hackerrank = models.TextField(db_column='HackerRank', blank=True, null=True)  # Field name made lowercase.
    hackerrank_score = models.IntegerField(db_column='HackerRank_Score', blank=True, null=True)  # Field name made lowercase.
    codeforces = models.TextField(db_column='CodeForces', blank=True, null=True)  # Field name made lowercase.
    codeforces_score = models.IntegerField(db_column='CodeForces_Score', blank=True, null=True)  # Field name made lowercase.
    codechef = models.TextField(db_column='CodeChef', blank=True, null=True)  # Field name made lowercase.
    codechef_score = models.IntegerField(db_column='CodeChef_Score', blank=True, null=True)  # Field name made lowercase.
    spoj = models.TextField(db_column='Spoj', blank=True, null=True)  # Field name made lowercase.
    spoj_score = models.IntegerField(db_column='Spoj_Score', blank=True, null=True)  # Field name made lowercase.
    interviewbit = models.TextField(db_column='InterviewBit', blank=True, null=True)  # Field name made lowercase.
    interviewbit_score = models.IntegerField(db_column='InterviewBit_Score', blank=True, null=True)  # Field name made lowercase.
    leetcode = models.TextField(db_column='LeetCode', blank=True, null=True)  # Field name made lowercase.
    leetcode_score = models.IntegerField(db_column='LeetCode_Score', blank=True, null=True)  # Field name made lowercase.
    gfg = models.TextField(db_column='GFG', blank=True, null=True)  # Field name made lowercase.
    gfg_score = models.IntegerField(db_column='GFG_Score', blank=True, null=True)  # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_score')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_scores'       
        
class Usernames(models.Model):
    user = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    hackerrank_username = models.CharField(max_length=50)
    codeforces_username = models.CharField(max_length=50)
    codechef_username = models.CharField(max_length=50)
    spoj_username = models.CharField(max_length=50)
    interviewbit_username = models.CharField(max_length=50)
    leetcode_username = models.CharField(max_length=50)
    gfg_username = models.CharField(max_length=50)
