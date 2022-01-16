from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from stdimage import StdImageField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='Publish')

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slika = StdImageField(upload_to='blog_slike', variations={'large': (1000, 560), 'thumbnail': (150, 150)}, delete_orphans=True, default='default.jpg')
    slug = models.SlugField(max_length=300, unique_for_date='created_at')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.created_at.year, self.created_at.month, self.created_at.day, self.slug])
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title