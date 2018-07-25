from django.db import models


# Create your models here.
class Category_Blog_article(models.Model):
    caption = models.CharField(max_length=20)


class ArticleType(models.Model):
    caption = models.CharField(max_length=20)


class Blog_article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1024)

    category = models.ForeignKey(Category_Blog_article)
    article_type = models.ForeignKey(ArticleType)
