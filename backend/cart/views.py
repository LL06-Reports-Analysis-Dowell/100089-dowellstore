import json
from rest_framework.decorators import api_view
from rest_framework import status
from product.dowellconnection1 import dowellconnection
from product.create_id import create_id
from rest_framework.response import Response

# Create your views here.

error_500_message = {"message": "Error processing your request, Retry"}


@api_view(["GET", "POST"])
def cart_list(request):

    field = {}

    if request.method == "POST":
        product_Id = request.data["productId"]
        quantity = request.data["quantity"]
        price = request.data["price"]
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ShoppingCart",
            "ShoppingCart",
            "1137",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_res = json.loads(res)
        cart_Id = create_id(json_res, "categoryId")
        cart_data = {
            "categoryId": cart_Id + 1,
            "productId": product_Id,
            "quantity": quantity,
            "price": price,
        }
        response = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ShoppingCart",
            "ShoppingCart",
            "1137",
            "ABCDE",
            "insert",
            cart_data,
            "nil",
        )
        json_response = json.load(response)
        return Response(response["data"])
    else:
        field = {}
        carts = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ShoppingCart",
            "ShoppingCart",
            "1137",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(carts)
        if len(json_data["data"]) < 1:
            return Response({"message": "No Carts were found"})
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
