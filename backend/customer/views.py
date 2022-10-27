import json
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# To make password encryption
from product.dowellconnection1 import dowellconnection
from product.create_id import create_id

error_500_message = {"message": "Error processing your request, Retry"}


@api_view(["GET"])
def home(request):
    return Response({"message": "Customer Endpoint is Up"})


# CUSTOMERS -----------------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def customer_list(request):
    field_add = {}

    if request.method == "POST":

        email = request.data["email"]
        name = request.data["name"]
        phone_number = request.data["phone_number"]
        address_line = request.data["addressLine"]
        city = request.data["city"]
        postal_code = request.data["postalCode"]
        country = request.data["country"]

        check_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Customer",
            "Customer",
            "1136",
            "ABCDE",
            "fetch",
            field_add,
            "nil",
        )
        json_check_data = json.loads(check_data)

        customer_id = create_id(json_check_data, "customerId")

        field = {
            "customerId": customer_id + 1,
            "name": name,
            "email": email,
            "phoneNumber": phone_number,
            "address": {
                "addressLine": address_line,
                "city": city,
                "postalCode": postal_code,
                "country": country,
            },
        }

        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Customer",
            "Customer",
            "1136",
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
            "Customer",
            "Customer",
            "1136",
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
def customer_detail(request, pk):
    field = {"customer_id": pk}

    if request.method == "PUT":

        email = request.data["email"]
        name = request.data["name"]
        phone_number = request.data["phone_number"]
        address_line = request.data["addressLine"]
        city = request.data["city"]
        postal_code = request.data["postalCode"]
        country = request.data["country"]

        update_field = {
            "customer_id": pk,
            "name": name,
            "email": email,
            "phone_number": phone_number,
             "address": {
                "addressLine": address_line,
                "city": city,
                "postalCode": postal_code,
                "country": country,
            },
        }

        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Customer",
            "Customer",
            "1136",
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
            "Customer",
            "Customer",
            "1136",
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
