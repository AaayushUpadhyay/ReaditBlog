from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Article,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    article=Article.objects.all()
    return render(request,'blog/articles.html',{'articles':article})


class PostListView(ListView):
    model=Article
    template_name='blog/articles.html' #app_name/model_listtype.html
    context_object_name='articles'
    paginate_by=3
    ordering = ['id']
   

def PostDetailView(request,pk):
    article=Article.objects.filter(id=pk).first()
    comments=Comment.objects.filter(article=article,parent=None)
    replies=Comment.objects.filter(article=article).exclude(parent=None)
    # un saari queries ko exclude kardo jaha parent none hai
    no=comments.count()
    
    return render(request,'blog/article_detail.html',{'comments':comments,'article':article,'no':no,'replies':replies})




    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Article #model_form.html
    fields=['title','content','image']
# abhi form submit nhi hoga kyunki hume post ka author nhi pata
    def form_valid(self,form):# we overwrite this function which by-default checks the validity of the form
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    fields=['title','content','image']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    success_url='/'
    def test_func(self): #model_confirm_delete.html
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def article(request):
    article=Article.objects.all()
    return render(request,'blog/detail.html',{'articles':article})

@login_required
def ArticleLike(request,pk):
    article=Article.objects.get(id=pk)
    current_user=request.user
    current_username=request.user.username
    already_liked=False
    already_disliked=False
    

    for i in article.likes.all():
        if i.username==current_username:
            already_liked=True
            break
    for j in article.dislikes.all():
        if j.username==current_username:
            already_disliked=True
            break
    
    if already_liked==True and already_disliked==True:
            article.dislikes.remove(current_user)
            article.likes.add(current_user)

            return HttpResponseRedirect(reverse('article-detail',args=[pk]))
    
    if already_liked==False and already_disliked==False:
        article.likes.add(current_user)
        return HttpResponseRedirect(reverse('article-detail',args=[pk]))
    
    else:
        if already_liked==False and already_disliked==True:
            article.dislikes.remove(current_user)
            article.likes.add(current_user)
            return HttpResponseRedirect(reverse('article-detail',args=[pk]))
        
        if already_liked==True and already_disliked==False:
            return HttpResponseRedirect(reverse('article-detail',args=[pk]))
        
        
            
       



    
    
    
        

   
@login_required           
def ArticleDislike(request,pk):
    article=Article.objects.get(id=pk)
    current_user=request.user
    current_username=request.user.username
    already_liked=False
    already_disliked=False
    

    for i in article.likes.all():
        if i.username==current_username:
            already_liked=True
            break
    for j in article.dislikes.all():
        if j.username==current_username:
            already_disliked=True
            break
    
    if already_liked==True and already_disliked==True:
            article.likes.remove(current_user)
            article.dislikes.add(current_user)

            return HttpResponseRedirect(reverse('article-detail',args=[pk]))
    
    if already_liked==False and already_disliked==False:
        article.dislikes.add(current_user)
        return HttpResponseRedirect(reverse('article-detail',args=[pk]))
    
    else:
        if already_liked==False and already_disliked==True:
            return HttpResponseRedirect(reverse('article-detail',args=[pk]))
        
        if already_liked==True and already_disliked==False:
            article.likes.remove(current_user)
            article.dislikes.add(current_user)
            return HttpResponseRedirect(reverse('article-detail',args=[pk]))

class MyArticles(LoginRequiredMixin,ListView):
    model=Article
    template_name='blog/myarticles.html' #app_name/model_listtype.html
    context_object_name='articles'
    paginate_by=3
    success_url='/'
   
    


            
@login_required
def ArticleComment(request):
    comments=Comment.objects.all()
    if request.method=='POST':
        article_id=request.POST.get('id')
        user=request.user
        parentSno=request.POST.get('parentSno')
        comment=request.POST.get('comment')
        if parentSno=="":
            submit_comment=Comment(article=Article.objects.get(id=article_id),content=comment,user=user)
            submit_comment.save()
            messages.success(request,f'Your comment has been submitted successfully !')
        else:
            submit_comment=Comment(article=Article.objects.get(id=article_id),content=comment,user=user,parent=Comment.objects.get(id=parentSno))
            submit_comment.save()
            messages.success(request,f'Your reply has been submitted successfully !')

            

        


       

       
        
    return HttpResponseRedirect(reverse('article-detail',args=[article_id]))



def CommentDelete(request,pk,x):
    c=Comment.objects.get(id=pk)
    if c.parent==None:
        c.delete()
        messages.success(request,f'Your comment has been deleted successfully !')
    else:
        c.delete()
        messages.success(request,f'Your reply has been deleted successfully !')
    
    return HttpResponseRedirect(reverse('article-detail',args=[x]))


