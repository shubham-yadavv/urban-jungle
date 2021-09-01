from django.shortcuts import render
from django.views import View
from selenium import webdriver

from .models import MenuItem, Category, OrderModel
from selenium import webdriver
from django.core.mail import send_mail
from django.conf import settings

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request,'about.html')



class Order(View):
    def get(self, request, *args, **kwargs):
        veg = MenuItem.objects.filter(category__name__contains='Veg')
        nonveg = MenuItem.objects.filter(category__name__contains='Nonveg')
        desserts = MenuItem.objects.filter(category__name__contains='Desserts')
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')


        context = {
            'veg' : veg,
            'nonveg' : nonveg,
            'desserts' : desserts,
            'drinks' : drinks,
        }

        return render(request, 'order.html', context)

    
    def post(self, request, *args, **kwargs):
        order_items = {
            'items' : []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }
  
        return render(request,'order_confirmation.html', context)

class User(View):
     def get(self, request, *args, **kwargs):
         if request.method == "GET":
             name = request.GET.get('fname')
             phno = request.GET.get('phno')
             email = request.GET.get('email')
             print(name,email)
         send_mail(
            'Order Confirmation',
            'Hello ' + name + ", \n Your order has been submitted. \nThank you for your support. \n\n\n\nThanks and Regards,\nUrban Jungle",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)


         return render(request, 'checkout.html')



class Final(View):
     def get(self, request, *args, **kwargs):
         return render(request,'info.php')
