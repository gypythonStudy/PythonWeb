from django.shortcuts import render
from  .models import Topic

# Create your views here.

def index(request):
    return  render(request,'blog/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return  render(request,'blog/topics.html',context)
def indexMe(request):
    return  render(request,'blog/index.html')
def info(request):
    return  render(request,'blog/info.html')
def about(request):
    return  render(request,'blog/about.html')
def gbook(request):
    return  render(request,'blog/gbook.html')
def life(request):
    return  render(request,'blog/life.html')
def list(request):
    return  render(request,'blog/list.html')
def share(request):
    return  render(request,'blog/share.html')
def time(request):
    return  render(request,'blog/time.html')