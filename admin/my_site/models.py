from django.db import models

class Toppage(models.Model):
    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=255)
    article = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'toppage'
        verbose_name_plural = 'toppage'