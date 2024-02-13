from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Oic1sIQ0qr3vSUKF8dP1pHtBpg61hBQ0Qtr7oHWmuPNHI2CNwBR2PM09m6lpuPwgfwAWgW6m5ClOEA749RtDDFw00HtqXbds1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)