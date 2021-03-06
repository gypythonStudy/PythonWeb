from django.db.models import QuerySet
from django.shortcuts import render,get_object_or_404
from  .models import Topic,Ghomeentry
from django.views import View
from pure_pagination import PageNotAnInteger, Paginator
import markdown
from learning_logs.models import Category,Blog,Comment,Counts
# Create your views here.

def index(request):
    homeModel = Ghomeentry.objects.order_by('date_public')
    bannerModel = Ghomeentry.objects.order_by('')
    context = {'homeModle': homeModel}
    return  render(request,'blog/index.html',context)

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return  render(request,'blog/topics.html',context)
def indexMe(request):
    homeModel = Ghomeentry.objects.order_by('date_public')
    context = {'homeModle': homeModel}
    return render(request, 'blog/index.html', context)
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
# def blog(request):
#     return  render(request,'blog/blogDetail.html')


#配置404 500错误页面
def page_not_found(request):
    return render(request, 'blog/404.html')


def page_errors(request):
    return render(request, 'blog/500.html')

class IndexView(View):
    """
    首页
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        # click_nums
        banner_blog = Blog.objects.order_by('-click_nums')[0:3]
        rigth_blog = Blog.objects.filter(click_nums=0)[0:2]
        # 轮播
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        count_nums.save()

        for blog in all_blog:
            blog.subContent = blog.content
            blog.content = markdown.markdown(blog.content,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
            # blog.subContent = blog.content


        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 2, request=request)
        all_blog = p.page(page)
        # b = Paginator(banner_blog, 2, request=request)
        # banner_blog = b.page(page)
        content = {
            'all_blog': all_blog,
            'banner_blog': banner_blog,
            'rigth_blog': rigth_blog,
            'blog_nums': blog_nums,
            'cate_nums': cate_nums,
            'tag_nums': tag_nums,
        }
        return render(request, 'blog/index.html', content)



class BlogDetailView(View):

    def get(self,request,blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        # 博客点击数+1, 评论数统计
        blog.click_nums += 1
        blog.save()
        # 获取评论内容
        all_comment = Comment.objects.filter(blog_id=blog_id)
        comment_nums = all_comment.count()
        # 将博客内容用markdown显示出来
        blog.content = markdown.markdown(blog.content,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
        # 实现博客上一篇与下一篇功能
        has_prev = False
        has_next = False
        id_prev = id_next = int(blog_id)
        blog_id_max = Blog.objects.all().order_by('-id').first()
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first()
            if not blog_prev:
                id_prev -= 1
            else:
                has_prev = True
        while not has_next and id_next <= id_max:
            blog_next = Blog.objects.filter(id=id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True;

        return render(request, 'blog/blogDetail.html', {
            'blog': blog,
            'blog_prev': blog_prev,
            'blog_next': blog_next,
            'has_prev': has_prev,
            'has_next': has_next,
            'all_comment': all_comment,
            'comment_nums': comment_nums,
            'blog_nums': blog_nums,
            'cate_nums': cate_nums,
            'tag_nums': tag_nums,

        })