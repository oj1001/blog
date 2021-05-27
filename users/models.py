from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	img=models.ImageField(default="default.jpg",upload_to="profile_pics") 

	def __str__(self):
		return f"{self.user.username} profile"

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.img.path)
		if img.width>300 or img.height>300:
			op_size=(300,300)
			img.thumbnail(op_size)
			img.save(self.img.path)