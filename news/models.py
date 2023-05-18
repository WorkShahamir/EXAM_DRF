from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('account.Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_status(self):
        statuses = NewsStatus.objects.filter(news=self).values('status__name').annotate(count=models.Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']
        return result


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('account.Author', on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_status(self):
        statuses = CommentStatus.objects.filter(comment=self).values('status__name').annotate(count=models.Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']
        return result


class Status(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NewsStatus(models.Model):
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    author = models.ForeignKey('account.Author', on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)


class CommentStatus(models.Model):
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    author = models.ForeignKey('account.Author', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
