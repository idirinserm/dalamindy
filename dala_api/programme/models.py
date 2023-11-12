from django.db import models

class Programme(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Course(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Text(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='texts')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
