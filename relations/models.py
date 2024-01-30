from django.db import models


class BoysModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class GirlsModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    boys = models.OneToOneField(BoysModel, related_name='girls', on_delete=models.SET_NULL, null=True)
    categirue = models.OneToOneField(BoysModel, related_name='girls', on_delete=models.SET_NULL, null=True)
    categirue = models.OneToOneField(BoysModel, related_name='girls', on_delete=models.SET_NULL, null=True)
