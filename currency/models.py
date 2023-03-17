from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.conf import settings

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,  # new
      on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    amount = models.IntegerField(max_length=200,default=0)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

class Package(models.Model):
    # category = models.ForeignKey(Category, related_name='currencies',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    last_check_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Confirm(models.Model):
    wallet_received = models.CharField(max_length=300)
    amount = models.IntegerField()
    wallet_sent = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    cryptocurrency = models.TextField(blank=True, null=False)
    receiver_wallet = models.TextField(blank=True, null=False)
    amount = models.IntegerField(blank=True, null=False)


    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
