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
    roll_no = models.CharField(db_column='Roll_No', primary_key=True, max_length=11)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='Mobile_No', max_length=11, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    hackerrank_username = models.CharField(db_column='HackerRank_UserName', max_length=26, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    algorithms = models.IntegerField(db_column='Algorithms', blank=True, null=True)  # Field name made lowercase.
    codeforces_username = models.CharField(db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    cf_problems_solved = models.IntegerField(db_column='CF_Problems_Solved', blank=True, null=True)  # Field name made lowercase.
    cfps_20 = models.IntegerField(db_column='CFPS_20', blank=True, null=True)  # Field name made lowercase.
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