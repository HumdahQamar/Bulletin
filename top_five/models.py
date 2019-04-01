from django.db import models


class Query(models.Model):
    title = models.CharField(max_length=50, null=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
