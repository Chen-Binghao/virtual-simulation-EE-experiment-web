# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=10)
    uloginid = models.CharField(max_length=20, blank=True, null=True, unique = True)
    upassword = models.CharField(max_length=45, blank=True, null=True)
    jname = models.CharField(max_length=45, blank=True)
    ja = models.CharField(max_length=45, blank=True)
    name = models.CharField(max_length=45, blank=True)

    class Meta:
        db_table = 'user'


class Experiment(models.Model):
    eid = models.CharField(primary_key=True, max_length=10)
    ename = models.CharField(max_length=45, blank=True, null=True)
    econtent = models.CharField(max_length=200, blank=True,null=True)

    class Meta:
        db_table = 'experiment'


class ExperimentGrade(models.Model):
    egid = models.CharField(primary_key=True, max_length=10)
    experiment_eid = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='experiment_eid')
    user_uid = models.ForeignKey(User, models.DO_NOTHING, db_column='User_uid')
    grade = models.CharField(max_length=10,blank=True, null=True)

    class Meta:
        db_table = 'experimentgrade'

