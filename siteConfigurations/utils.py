from django.urls import get_resolver

def get_named_urls():
    exclude = ['remove_from_cart', 'add_to_cart', 'update_cart_quantity','products-by-category','product-details',]
    named_urls = []
    resolver = get_resolver()
    for name in resolver.reverse_dict.keys():
        if isinstance(name, str) and name not in exclude:
            named_urls.append((name, name))
    return sorted(named_urls)