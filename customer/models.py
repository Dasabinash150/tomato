from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CartItems(models.Model):
    cart_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField(blank=True, null=True)
    inst = models.CharField(max_length=50)


    class Meta:
        # Define unique constraint across field1 and field2
        unique_together = ('cart_id', 'item_name')
    def __str__(self):
        return self.item_name
    

#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         self.total_price = self.item.item_price * self.quantity
#         super().save(*args, **kwargs)

