from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from siteapp.models import product

# Create your views here.


def cart_detail(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total_price = 0

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

    return render(
        request,
        "cart/cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


def add_to_cart(request, product_id):
    product_obj = get_object_or_404(product, id=product_id)
    quantity = int(request.POST.get("quantity", 1))

    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    request.session["cart"] = cart
    return redirect("cart_detail")


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart_detail')
