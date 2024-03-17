from django.db import models
import datetime
from django.utils import timezone
class Blog(models.Model):
    blog_owner = models.CharField('владелец блога', max_length = 200)
    blog_owner_description = models.TextField('о себе')
    blog_car = models.CharField('автомобиль', max_length = 100)
    registration_date = models.DateTimeField('дата создания')
    
    def __str__(self):
        return self.blog_owner
    
    def was_registered(self):
        return self.registration_date >=(timezone.now())
   
    
class Post(models.Model):
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
    post_title = models.CharField('название поста', max_length = 200)
    post_text = models.TextField('текст поста')
    posted_date = models.DateTimeField('время записи')
    
    def was_posted_recently(self):
        return self.posted_date >= (timezone.now()-datetime.timedelta(days=7))
    def __str__(self):
        return self.post_title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    author_name = models.CharField('имя автора',max_length = 200)
    comment_text = models.TextField('текст комментария')
    comment_date = models.DateTimeField('время комментария')
    
    def __str__(self):
        return self.author_name