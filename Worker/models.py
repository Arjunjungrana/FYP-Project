
# Create your models here.
from django.db import models
from accounts.models import User, UserProfile

# Create your models here.
from django.utils.deconstruct import deconstructible


@deconstructible
class WorkerImagePath:
    def _init_(self, sub_path):
        self.sub_path = sub_path

    def _call_(self, instance, filename):
        # Generate the path and filename
        return f'Worker/{self.sub_path}/{instance.user.username}/{filename}'
class Worker(models.Model):
  CHOICES = (
           ("GARDENER", "Gardener"),
           ("ELECTRICIAN", "Electrician"),
           ("PANITER", "Painter"),
            )
  user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
  user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
  worker_certificate= models.ImageField(upload_to=WorkerImagePath('certificate'), blank=True, null=True)
  worker_description = models.TextField(blank=True, null=True)
  service_type = models.CharField(max_length=25, choices=CHOICES, default='GARDENER')
  service_description = models.TextField(blank=True, null=True)
  service_charge = models.IntegerField()
  service_image = models.ImageField(upload_to=WorkerImagePath('serviceImages'), blank=True, null=True)
  approval_status = models.BooleanField(default=False)
  available_status = models.BooleanField(default=False)
  booked_status = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def _str_(self):
    return self.user.username