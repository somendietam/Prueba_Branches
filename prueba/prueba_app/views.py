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

def agregar_a_cart(request, producto_id):
    """Agrega un producto al carrito del usuario."""
    user_email = request.session.get('user_email')  # Obtener el correo del usuario desde la sesión
    cart = get_object_or_404(Cart, user=user_email)

    # Aquí debes implementar la lógica para agregar el producto al carrito
    # Por ejemplo, agregar un nuevo item al carrito o incrementar la cantidad si ya existe

    # Simulación de agregar un producto (esto debería adaptarse a tus modelos)
    # cart.items.add(producto_id)  # Asegúrate de tener la relación definida

    cart.save()  # Guarda el carrito después de agregar el producto
    return redirect('ver_cart')  # Redirige a la vista del carrito