from djongo import models
# Create your models here.

class dataset(models.Model):
    _id=models.ObjectIdField()
    post_title=models.CharField(max_length=255)
    data_title=models.CharField(max_length=255)
    tags=models.JSONField()
    user_details=models.JSONField()
    objects=models.DjongoManager()


