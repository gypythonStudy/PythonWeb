from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry,Ghomeentry,Testentry


#注册model
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Ghomeentry)
admin.site.register(Testentry)