from django.shortcuts import render,get_object_or_404
from  .models import Topic,Ghomeentry
from django.views import View
from pure_pagination import PageNotAnInteger, Paginator

import markdown

# Create your views here.

def index(request):
    homeModel = Ghomeentry.objects.order_by('date_public')
    context = {'homeModle': homeModel}
    return  render(request,'blog/index.html',context)

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

#配置404 500错误页面
def page_not_found(request):
    return render(request, '404.html')


def page_errors(request):
    return render(request, '500.html')

class IndexView(View):
    """
    首页
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        count_nums.save()

        for blog in all_blog:
            blog.content = markdown.markdown(blog.content)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 5, request=request)
        all_blog = p.page(page)
        return render(request, 'blog/index.html', {
            'all_blog': all_blog,
            'blog_nums': blog_nums,
            'cate_nums': cate_nums,
            'tag_nums': tag_nums,
        })



class BlogDetailView(View):

    def get(self,request,blog_id):
        blog = get_object_or_404(Blog,pk=blog_id)