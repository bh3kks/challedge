from django.contrib import admin
from chatting.models import User, Comments, ChattingRoom

# Register your models here.
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(ChattingRoom)