from django.db import models


class service(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="image/")
    upload_to = models.DateTimeField(auto_now_add=True)
    h4 = models.CharField(max_length=555)
    p = models.CharField(max_length=555)
    link = models.CharField(max_length=555)

    def __str__(self):
        return self.h4
