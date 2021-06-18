from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextField(null=True,default=True)
    date_posted=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to="article_images")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name="blog_articles",blank=True)
    dislikes=models.ManyToManyField(User,related_name="blog_articles_dislike",blank=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article-detail',kwargs={'pk':self.pk})
    

    def fun(self):
        context={}
        context['comments']=self.comment_set.all()
        return context
    
    
    
    

    



class Comment(models.Model):
    content=models.TextField(max_length=500)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.content[0:13]+"...  "+"  by  "+self.user.username+" on "+self.article.title