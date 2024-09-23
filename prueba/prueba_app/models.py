from django.db import models

class Cart(models.Model):
    user = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)

    def __str__(self):
        return f"Carrito de {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
