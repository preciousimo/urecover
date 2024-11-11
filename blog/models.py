from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)  # Store tags as a JSON list
    published_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
