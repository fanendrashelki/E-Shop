
from django.shortcuts import redirect, render
from django.views import View
from store.models.orders import Order



class Orderview(View):
   
    def get(self ,request):
        customer=request.session.get('customer')
        orders=Order.get_orders_by_customer(customer)
        # print(order)
        # order= order.reverse()
        return render(request, 'app/order.html',{'orders':orders})
       