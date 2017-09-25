from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Post(models.Model):
    topic = models.ForeignKey(Topic)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(verbose_name='Text')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50]+'...'
        else:
            return self.text
