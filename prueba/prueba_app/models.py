from django.db import models

class Cart(models.Model):
    user = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)

    def __str__(self):
        return f"Carrito de {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())
