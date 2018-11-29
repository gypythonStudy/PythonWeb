from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry,Ghomeentry,Testentry,Counts,Comment,Blog,Tag,Category


#注册model
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Ghomeentry)
admin.site.register(Testentry)

admin.site.register(Counts)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)