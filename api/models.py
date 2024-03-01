from django.db import models

class Toifalash(models.Model):
    dars = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dars


class PDFFile(models.Model):
    file = models.FileField(upload_to='pdf_files/')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class VideoFile(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='video_files/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class VideoFile(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     file = models.FileField(upload_to='video_files/')
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title



class Test(models.Model):
    toifalash = models.ForeignKey(Toifalash, on_delete=models.CASCADE, null=True, blank=True)
    test = models.CharField(max_length=255)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    t_j = models.CharField(max_length=100)

    def __str__(self):
        return self.test