from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from siteapp.models import product
from decimal import Decimal
from django.http import JsonResponse


def cart_detail(request):
    # categories = category.objects.all()
    cart = request.session.get("cart", {})
    cart_items = []
    total_price = 0
    cargo_price = Decimal("232.00")

    for product_id, quantity in cart.items():
        prod = product.objects.get(id=product_id)
        subtotal = prod.price * quantity
        total_price += subtotal

        cart_items.append(
            {
                "product": prod,
                "quantity": quantity,
                "subtotal": subtotal,
                "image": prod.image.url if prod.image else None,
            }
        )

    total_without_cargo = total_price + cargo_price

    return render(
        request,
        "cart/cart.html",
        {
            "cart_items": cart_items,
            "total_price": total_price,
            "total_without_cargo": total_without_cargo,
            "cargo_price": cargo_price,
            # "categories": categories,
        },
    )

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart_detail')

def update_cart_quantity(request, product_id):
    if request.method == "POST":
        action = request.POST.get("action")
        cart = request.session.get("cart", {})

        quantity = cart.get(str(product_id), 0)

        if action == "increase":
            quantity += 1
        elif action == "decrease" and quantity > 1:
            quantity -= 1

        cart[str(product_id)] = quantity
        request.session["cart"] = cart

    return redirect("cart_detail")

def add_to_cart(request, product_id):
    product_obj = get_object_or_404(product, id=product_id)
    quantity = int(request.POST.get("quantity", 1))

    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    request.session["cart"] = cart
    request.session.modified = True

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Sepetteki toplam ürün sayısını hesapla
        total_items = sum(cart.values())
        return JsonResponse({
            'success': True,
            'cart_item_count': total_items,
            'message': 'Ürün sepete eklendi'
        })
    
    return redirect("products")


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session["cart"] = cart
    return redirect("cart_detail")
