from django.db import models

class FoodsModel(models.Model):
    image1 = models.ImageField(upload_to='foods')
    image2 = models.ImageField(upload_to='foods')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    discount_price = models.FloatField(null=True, blank=True)
    is_special = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Foods'
        verbose_name = 'Food'

