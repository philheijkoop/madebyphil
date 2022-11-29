from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    author = models.CharField(default="Phil", max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField()
    publish_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    published = models.BooleanField(default=False)
    draft = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    series_number = models.IntegerField(default=0)
    raw_markdown = models.TextField()


