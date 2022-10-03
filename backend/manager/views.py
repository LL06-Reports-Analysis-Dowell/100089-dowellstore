from django.shortcuts import render

from grocery.dowellconnection1 import dowellconnection


# Create your views here.
def home(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']
        industry = request.POST['industry']
        about = request.POST['about']
        event_delivery_type = request.POST['event_delivery_type']
        event_menu_type = request.POST['event_menu_type']
        delivery_counters = request.POST['delivery_counters']
        repeat_menu = request.POST['repeat_menu']
        customer_language = request.POST['customer_language']
        payment_option = request.POST['payment_option']
        brand_logo = request.POST['brand_logo']

        field = {
            "brand_name": brand_name,
            "industry": industry,
            "about": about,
            "event_delivery_type": event_delivery_type,
            "event_menu_type": event_menu_type,
            "delivery_counters": delivery_counters,
            "repeat_menu": repeat_menu,
            "customer_language": customer_language,
            "payment_option": payment_option,
            "brand_logo": brand_logo
        }

        print(field)

        # res = dowellconnection()

    return render(request, 'manager/index.html')
