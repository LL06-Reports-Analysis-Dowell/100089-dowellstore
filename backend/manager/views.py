import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# To make password encryption
from django.contrib.auth.hashers import make_password
from grocery.dowellconnection1 import dowellconnection
from grocery.create_id import create_id

error_500_message = {"message": "Error processing your request, Retry"}


# Create your views here.
def home(request):
    if request.method == "POST":
        brand_name = request.POST["brand_name"]
        industry = request.POST["industry"]
        about = request.POST["about"]
        event_delivery_type = request.POST["event_delivery_type"]
        event_menu_type = request.POST["event_menu_type"]
        delivery_counters = request.POST["delivery_counters"]
        repeat_menu = request.POST["repeat_menu"]
        customer_language = request.POST["customer_language"]
        payment_option = request.POST["payment_option"]
        brand_logo = request.POST["brand_logo"]

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
            "brand_logo": brand_logo,
        }

        print(field)

        # res = dowellconnection()

    return render(request, "manager/index.html")


# VENDORS ------------------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def vendor_list(request):
    field_add = {}

    if request.method == "POST":

        name = request.data["name"]
        email = request.data["email"]
        description = request.data["description"]
        company_code = request.data["company_code"]
        address_street_no = request.data["address_street_no"]
        address_street_alt = request.data["address_street_alt"]
        address_city = request.data["address_city"]
        address_state = request.data["address_state"]
        address_postal_code = request.data["address_postal_code"]
        address_country_code = request.data["address_country_code"]

        check_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductVendor",
            "ProductVendor",
            "1135",
            "ABCDE",
            "insert",
            field_add,
            "nil",
        )
        json_check_data = json.loads(check_data)
        print(json_check_data)

        vendor_id = create_id(json_check_data, "vendor_id")

        field = {
            "vendor_id": vendor_id + 1,
            "name": name,
            "email": email,
            "description": description,
            "company_code": company_code,
            "address_street_no": address_street_no,
            "address_street_alt": address_street_alt,
            "address_city": address_city,
            "address_state": address_state,
            "address_postal_code": address_postal_code,
            "address_country_code": address_country_code,
        }

        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductVendor",
            "ProductVendor",
            "1135",
            "ABCDE",
            "insert",
            field,
            "nil",
        )
        res1 = json.loads(res)

        return Response(res1, status=status.HTTP_201_CREATED)

    else:

        data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductVendor",
            "ProductVendor",
            "1135",
            "ABCDE",
            "fetch",
            field_add,
            "nil",
        )
        json_data = json.loads(data)

        if len(json_data["data"]) < 1:

            return Response(
                {"message": "No customers were found"}, status=status.HTTP_404_NOT_FOUND
            )

        elif len(json_data["data"]) >= 1:

            return Response(json_data["data"], status=status.HTTP_200_OK)

        else:

            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["GET", "PUT"])
def vendor_detail(request, pk):
    field = {"vendor_id": pk}

    if request.method == "PUT":

        name = request.data["name"]
        email = request.data["email"]
        description = request.data["description"]
        company_code = request.data["company_code"]
        address_street_no = request.data["address_street_no"]
        address_street_alt = request.data["address_street_alt"]
        address_city = request.data["address_city"]
        address_state = request.data["address_state"]
        address_postal_code = request.data["address_postal_code"]
        address_country_code = request.data["address_country_code"]

        update_field = {
            "vendor_id": pk,
            "name": name,
            "email": email,
            "description": description,
            "company_code": company_code,
            "address_street_no": address_street_no,
            "address_street_alt": address_street_alt,
            "address_city": address_city,
            "address_state": address_state,
            "address_postal_code": address_postal_code,
            "address_country_code": address_country_code,
        }

        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductVendor",
            "ProductVendor",
            "1135",
            "ABCDE",
            "update",
            field,
            update_field,
        )
        res1 = json.loads(res)

        return Response(res1, status=status.HTTP_200_OK)

    else:

        customer = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductVendor",
            "ProductVendor",
            "1135",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(customer)

        if len(json_data["data"]) < 1:

            return Response(
                {"message": "Profile Requested Not Found!"},
                status=status.HTTP_404_NOT_FOUND,
            )

        elif len(json_data["data"]) >= 1:

            return Response(json_data["data"], status=status.HTTP_200_OK)

        else:

            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
