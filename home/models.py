from django.db import models

# Create your models here.


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
    hackerrank_score = models.IntegerField(db_column='HackerRank_Score')  # Field name made lowercase.
    codeforces = models.TextField(db_column='CodeForces', blank=True, null=True)  # Field name made lowercase.
    codeforces_score = models.IntegerField(db_column='CodeForces_Score')  # Field name made lowercase.
    codechef = models.TextField(db_column='CodeChef', blank=True, null=True)  # Field name made lowercase.
    codechef_score = models.IntegerField(db_column='CodeChef_Score')  # Field name made lowercase.
    spoj = models.TextField(db_column='Spoj', blank=True, null=True)  # Field name made lowercase.
    spoj_score = models.IntegerField(db_column='Spoj_Score')  # Field name made lowercase.
    interviewbit = models.TextField(db_column='InterviewBit', blank=True, null=True)  # Field name made lowercase.
    interviewbit_score = models.IntegerField(db_column='InterviewBit_Score')  # Field name made lowercase.
    leetcode = models.TextField(db_column='LeetCode', blank=True, null=True)  # Field name made lowercase.
    leetcode_score = models.IntegerField(db_column='LeetCode_Score')  # Field name made lowercase.
    gfg = models.TextField(db_column='GFG', blank=True, null=True)  # Field name made lowercase.
    gfg_score = models.IntegerField(db_column='GFG_Score')  # Field name made lowercase.
    overall_score = models.IntegerField(db_column='Overall_score')  # Field name made lowercase.
    daily_scores = models.TextField(blank=True, null=True)       

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
    
    
class Announcement(models.Model):
    text_input = models.CharField(max_length=200)
    date_input = models.DateField()
    
    def __str__(self):
        return self.text_input

class Averages(models.Model):
    averages = models.CharField(db_column='Averages', primary_key=True, max_length=45)  # Field name made lowercase.
    cse = models.DecimalField(max_digits=10, decimal_places=2)
    it = models.DecimalField(max_digits=10, decimal_places=2)
    ece = models.DecimalField(max_digits=10, decimal_places=2)
    eee = models.DecimalField(max_digits=10, decimal_places=2)
    csm = models.DecimalField(max_digits=10, decimal_places=2)
    aiml = models.DecimalField(max_digits=10, decimal_places=2)
    mec = models.DecimalField(max_digits=10, decimal_places=2)
    civ = models.DecimalField(max_digits=10, decimal_places=2)
    aids = models.DecimalField(max_digits=10, decimal_places=2)
    college = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'averages'
