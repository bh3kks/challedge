from django.db import models

class User(models.Model):
    username = models.TextField(max_length=20, blank=False)
    created = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    # 채팅 한 마디
    user = models.ForeignKey(User)
    content = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)

class ChattingRoom(models.Model):
    # 대학교별 채팅 방
    name = models.TextField(max_length=50, blank=False)
    max_user = models.IntegerField(null=30)
    cur_user = models.IntegerField(null=0)