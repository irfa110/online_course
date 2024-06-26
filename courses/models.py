from django.db import models
from django.contrib.auth.models import User
# u - admin
# p - 12345

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50,null = False)
    slug = models.CharField(max_length=50,null = False,unique=True)
    description = models.CharField(max_length = 200, null = True)
    price = models.PositiveIntegerField(null=False)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=False)
    thumbnail =models.ImageField(upload_to='files/thumbnail')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resource')
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    cource = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_url = models.CharField(max_length = 100,null=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Usercourse(models.Model):
    user  = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"


class Payment(models.Model):
    order_id = models.CharField(max_length=100,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    user_course = models.ForeignKey(Usercourse,null=True,blank =True,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id