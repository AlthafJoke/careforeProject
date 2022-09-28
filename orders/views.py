
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from Grocery.models import CartItem, Cart
from .models import Order, OrderProduct, Payment
from .forms import OrderForm
import datetime 
# from Grocery.views import _cart_id
import json



# Create your views here.
def payments(request):
    body = json.loads(request.body)

    order_id = body['orderID'].strip()
    order = Order.objects.get(is_ordered=False, order_number= order_id)
    
    
    
    
    # store transaction details in the payment model
    payment = Payment(
        user = order.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid  = order.order_total,
        status = body['status'],
    )
    payment.save()
    print(payment)
    order.payment = payment
    order.is_ordered = True
    order.save()
    
    # move the cart items in Order Product table
    cart_item =CartItem.objects.filter(user=request.user)
    
    for item in cart_item:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.price
        orderproduct.ordered = True
        orderproduct.save()
        
        
        
        
        
      
    
    
    #reduce the quantity of the sold products
    
    #clear cart
    
    #send order recieved email to customer
    
    #send order number and transaction id back to send data method via JSONresponse 
    
    return render(request, 'orders/payments.html')







def place_order(request, total=0, quantity=0,):
    current_user = request.user
    # cart = Cart.objects.get(cart_id=_cart_id(request))
    
    grand_total = 0
    tax = 0
    delivery_charge = 50
    
    cart = Cart.objects.get(cart_id = _cart_id(request))   
    cart_items = CartItem.objects.filter(Cart=cart, is_active=True)
    print(cart_items)
    for cart_item in cart_items:
        print("inside for loop")
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
        print("hello")
        
    print("total is :",total)
    tax = (3 * total) / 100
    
    # total_after_tax = total + tax
    
    grand_total = total + delivery_charge + tax
    
    
    
    if request.method == "POST":
        print("Post is working")
        form = OrderForm(request.POST)
        if form.is_valid():
            #store billing details information inside order table
            data = Order()
            data.first_name     = form.cleaned_data['first_name']
            data.last_name      = form.cleaned_data['last_name']
            data.phone          = form.cleaned_data['phone']
            data.email          = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country        = form.cleaned_data['country']
            data.state          = form.cleaned_data['state']
            data.city           = form.cleaned_data['city']
            data.order_note     = form.cleaned_data['order_note']
            data.order_total    = grand_total
            data.tax            = tax
            data.ip            = request.META.get('REMOTE_ADDR')
            # data.product_total = total_after_tax
            data.user = request.user
            data.save()
            
            
             #genarate order number and store in order table
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d  = datetime.date(yr, mt, dt)
            current_date = d.strftime("%d%m%Y") # like 20220305
             
            order_number = current_date + str(data.id)
            name = data.first_name
            address = data.address_line_1
            
            data.order_number = order_number
            data.save()
            order = Order.objects.get(order_number=order_number)
            
            context = {
                'order':order,
                'cart_items':cart_items,
                'total':total,
                'tax': tax,
                'grand_total':grand_total,
                'name':name,
                'address':address,
            }
           
            return render(request, 'orders/payments.html', context)
        
        else:
            # return redirect('checkout')
            return HttpResponse("form is invalid")
    
    #if the cart item is less than or equal to  0 then redirect to shop or home

    cart_count = cart_items.count()
    if cart_count <= 0:
        
        return HttpResponse("your cart is empty")
   
    
            
            
