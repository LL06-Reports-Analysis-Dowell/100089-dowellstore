import json
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from product.dowellconnection1 import dowellconnection
from product.create_id import create_id

error_500_message = {"message": "Error processing your request, Retry"}
# Create your views here.
@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        field = {}
        categories = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1133",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(categories)
        if len(json_data["data"]) < 1:
            return Response({"message": "No Products Categories were found"})
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    if request.method == "POST":
        customer = request.POST["customer"]
        products = request.POST["products"]
        shippingAddress = request.POST["shippingAddress"]
        paymentMethod = request.POST["paymentMethod"]
        itemPrice = request.POST["itemPrice"]
        shippingPrice = request.POST["shippingPrice"]
        taxPrice = request.POST["taxPrice"]
        isPaid = request.POST["isPaid"]
        status = request.POST["status"]
        paidAt = request.POST["paidAt"]
        deliveredAt = request.POST["deliveredAt"]
        test_data = {}
        category_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1133",
            "ABCDE",
            "fetch",
            test_data,
            "nil",
        )
        json_category_data = json.loads(category_data)
        orderId = create_id(json_category_data, "orderId")
        order = {
            "orderId": orderId + 1,
            "customerId": customer,
            "products": [
                {
                    "name": products.name,
                    "sku": products.sku,
                    "description": products.description,
                }
            ],
            "shippingAddress": [
                {
                    "address": shippingAddress.address,
                    "city": shippingAddress.city,
                    "country": shippingAddress.country,
                }
            ],
            "paymentMethod": paymentMethod,
            "itemPrice": itemPrice,
            "shippingPrice": shippingPrice,
            "taxPrice": taxPrice,
            "isPaid": isPaid,
            "paidAt": paidAt,
            "deliveredAt": deliveredAt,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1133",
            "ABCDE",
            "insert",
            order,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)


def order_detail(request, pk):
    field = {"orderId": pk}
    if request.method == "GET":
        order = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1132",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(order)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    elif request.method == "PUT":
        customer = request.POST["customer"]
        products = request.POST["products"]
        shippingAddress = request.POST["shippingAddress"]
        paymentMethod = request.POST["paymentMethod"]
        itemPrice = request.POST["itemPrice"]
        shippingPrice = request.POST["shippingPrice"]
        taxPrice = request.POST["taxPrice"]
        isPaid = request.POST["isPaid"]
        status = request.POST["status"]
        paidAt = request.POST["paidAt"]
        deliveredAt = request.POST["deliveredAt"]

        update_order = {
            "orderId": pk,
            "customerId": customer,
            "products": [
                {
                    "name": products.name,
                    "sku": products.sku,
                    "description": products.description,
                }
            ],
            "shippingAddress": [
                {
                    "address": shippingAddress.address,
                    "city": shippingAddress.city,
                    "country": shippingAddress.country,
                }
            ],
            "paymentMethod": paymentMethod,
            "itemPrice": itemPrice,
            "shippingPrice": shippingPrice,
            "taxPrice": taxPrice,
            "isPaid": isPaid,
            "paidAt": paidAt,
            "deliveredAt": deliveredAt,
        }
        order = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1132",
            "ABCDE",
            "update",
            field,
            update_order,
        )
        return Response(status=status.HTTP_200_OK)

def customer_order(request, customer_pk):
    field = {"customerId": customer_pk}
    if request.method == "GET":
        order = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Order",
            "Order",
            "1132",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(order)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "orders not found"}, status=status.HTTP_404_NOT_FOUND
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )