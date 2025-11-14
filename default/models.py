from django.db import models

# Create your models here.
class Poll(models.Model):    #建立群組套用模型
    subject = models.CharField("投票主題",max_length=64)    #引用模型單行文字取名字
    desc = models.TextField("說明")  #多行文字
    created = models.DateField("建立日期",auto_now_add=True)   #第一次建立時間

class Option(models.Model):
    title = models.CharField("選項文字",max_length=64)
    votes = models.IntegerField("票數", default=0) #預設值為0
    poll_id = models.IntegerField("投票主題編號")