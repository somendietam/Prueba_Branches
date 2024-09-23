from django.shortcuts import render, redirect,get_object_or_404
from .models import *

def index(request):
    context = {}
    return render(request, 'gravity_app/index.html', context)
def ver_cart(request):
    """Muestra el carrito de compras del usuario."""
    # Supongamos que el usuario está autenticado y lo obtenemos de la sesión
    user_email = request.session.get('user_email')  # Aquí asumo que estás usando sesiones para almacenar el correo del usuario
    cart = get_object_or_404(Cart, user=user_email)
    
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)
