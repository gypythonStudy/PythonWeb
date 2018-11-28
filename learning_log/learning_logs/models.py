from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return  self.text

class Entry(models.Model):

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):

        return self.text[:50] + "..."
#
class Ghomeentry(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    userName = models.CharField(max_length=50)
    typeName = models.CharField(max_length=50)
    date_public = models.DateTimeField(auto_now_add=True)
    read_num = models.IntegerField()
    imageName = models.CharField(max_length=50)

    # def __str__(self):
    #
    #     return self

class Testentry(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    userName = models.CharField(max_length=50)
    typeName = models.CharField(max_length=50)
    date_public = models.DateTimeField(auto_now_add=True)
    read_num = models.IntegerField()
    imageName = models.CharField(max_length=50)

    # def __str__(self):
    #
    #     return self


