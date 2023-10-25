# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branch(models.Model):
    # Field name made lowercase.
    branch_id = models.IntegerField(db_column='Branch_id', primary_key=True)
    # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=45)

    class Meta:
        managed = False
        db_table = 'branch'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class R21(models.Model):
    # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)
    # Field name made lowercase.
    roll_number = models.CharField(
        db_column='Roll_Number', primary_key=True, max_length=12)
    # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=39,
                            db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    branch = models.CharField(
        db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16,
                                db_collation='utf8mb3_general_ci', blank=True, null=True)
    # Field name made lowercase.
    last_login = models.DateField(
        db_column='LAST_LOGIN', blank=True, null=True)
    # Field name made lowercase.
    mobile = models.BigIntegerField(db_column='Mobile')
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=45, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    hackerrank_username = models.CharField(
        db_column='HackerRank_UserName', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    algorithms = models.CharField(db_column='Algorithms', max_length=16)
    # Field name made lowercase.
    codechef_username = models.CharField(
        db_column='CodeChef_UserName', max_length=19)
    # Field name made lowercase.
    cc_problems_solved = models.IntegerField(db_column='CC_Problems_Solved')
    # Field name made lowercase.
    codeforces_username = models.CharField(
        db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    cf_problems_solved = models.IntegerField(db_column='CF_Problems_Solved')
    # Field name made lowercase.
    spoj_username = models.CharField(
        db_column='Spoj_UserName', max_length=19, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    spoj_problems_solved = models.IntegerField(
        db_column='Spoj_Problems_Solved')
    # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_Score')
    # Field name made lowercase.
    ccps_10 = models.IntegerField(db_column='CCPS_10')
    # Field name made lowercase.
    cfps_10 = models.IntegerField(db_column='CFPS_10')
    # Field name made lowercase.
    sps_20 = models.IntegerField(db_column='SPS_20')

    class Meta:
        managed = False
        db_table = 'r21'


class R22(models.Model):
    # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)
    # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=31,
                            db_collation='utf8mb3_general_ci', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=54,
                             db_collation='utf8mb3_general_ci', blank=True, null=True)
    # Field name made lowercase.
    roll_no = models.CharField(
        db_column='Roll_No', primary_key=True, max_length=11)
    # Field name made lowercase.
    mobile_no = models.CharField(
        db_column='Mobile_No', max_length=11, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    branch = models.CharField(
        db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    hackerrank_username = models.CharField(
        db_column='HackerRank_UserName', max_length=26, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    algorithms = models.IntegerField(
        db_column='Algorithms', blank=True, null=True)
    # Field name made lowercase.
    codeforces_username = models.CharField(
        db_column='Codeforces_UserName', max_length=24, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    cf_problems_solved = models.IntegerField(
        db_column='CF_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    cfps_20 = models.IntegerField(db_column='CFPS_20', blank=True, null=True)
    # Field name made lowercase.
    codechef_username = models.CharField(
        db_column='CodeChef_UserName', max_length=19, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    cc_problems_solved = models.IntegerField(
        db_column='CC_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    ccps_10 = models.IntegerField(db_column='CCPS_10', blank=True, null=True)
    # Field name made lowercase.
    spoj_username = models.CharField(
        db_column='Spoj_UserName', max_length=18, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    spoj_problems_solved = models.IntegerField(
        db_column='Spoj_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    sps_20 = models.IntegerField(db_column='SPS_20', blank=True, null=True)
    # Field name made lowercase.
    interviewbit_username = models.CharField(
        db_column='InterviewBit_Username', max_length=37, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    ib_problems_solved = models.IntegerField(
        db_column='IB_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    ib_10 = models.IntegerField(db_column='IB_10', blank=True, null=True)
    # Field name made lowercase.
    leetcode_username = models.CharField(
        db_column='LeetCode_Username', max_length=23, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    leet_problems_solved = models.IntegerField(
        db_column='Leet_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    lp_10 = models.IntegerField(db_column='LP_10', blank=True, null=True)
    # Field name made lowercase.
    geeksforgeeks_username = models.CharField(
        db_column='GeeksForGeeks_Username', max_length=24, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    gfg_problems_solved = models.IntegerField(
        db_column='GFG_Problems_Solved', blank=True, null=True)
    # Field name made lowercase.
    gfg_10 = models.IntegerField(db_column='GFG_10', blank=True, null=True)
    # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_Score')

    class Meta:
        managed = False
        db_table = 'r22'


class UserScores(models.Model):
    # Field name made lowercase.
    roll_number = models.CharField(
        db_column='Roll_Number', primary_key=True, max_length=10, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=34,
                            db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    branch = models.CharField(
        db_column='Branch', max_length=7, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    mobile = models.BigIntegerField(db_column='Mobile', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=37, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    hackerrank_hr = models.CharField(
        db_column='HackerRank_HR', max_length=16, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    hackerrank_algo = models.IntegerField(
        db_column='HackerRank_Algo', blank=True, null=True)
    # Field name made lowercase.
    codechef_cc = models.CharField(
        db_column='CodeChef_CC', max_length=14, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    cc_problems = models.IntegerField(
        db_column='CC_problems', blank=True, null=True)
    # Field name made lowercase.
    cc_score = models.IntegerField(db_column='CC_score', blank=True, null=True)
    # Field name made lowercase.
    codeforces_cf = models.CharField(
        db_column='Codeforces_CF', max_length=20, db_collation='utf8mb3_general_ci')
    # Field name made lowercase.
    cf_problems = models.IntegerField(
        db_column='CF_problems', blank=True, null=True)
    # Field name made lowercase.
    cf_score = models.IntegerField(db_column='CF_score', blank=True, null=True)
    # Field name made lowercase.
    overall_score = models.IntegerField(
        db_column='Overall_Score', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_scores'
