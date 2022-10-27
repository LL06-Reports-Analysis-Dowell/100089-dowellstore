# import base64
import json
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .dowellconnection1 import dowellconnection
from .create_id import create_id
from .models import Product

error_500_message = {"message": "Error processing your request, Retry"}


# Home Routes ------------------------------------------------------------------
def api_home(request):
    return JsonResponse({"message": "The API Endpoint is Up"})


# PRODUCT ------------------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def product_list(request):
    """
    get:
    Product List

    post:
    Create a new Product.
    """
    if request.method == "POST":
        name = request.data["name"]
        sku = request.data["sku"]
        slug = name.replace(" ", "-")
        countInStock = request.data["countInStock"]
        categoryId = request.data["categoryId"]
        description = request.data["description"]
        # Handle Product Image
        if "image" in request.FILES.keys():
            image = request.FILES["image"]
            product = Product(
                image=image,
                sku=sku,
                description=description,
            )
            Product.save(product)
            image_name = f"media/product/{image}"
        else:
            image_name = "media/yourlogo.png"
            # Convert Image to base64
            # Fix Some Test Failing: If the Image name has spaces
            # with open(f"media/product_images/{image}", "rb") as our_image:
            #     # print(our_image)
            #     converted_string = base64.b64encode(our_image.read())
            #     print(converted_string.decode('utf-8'))
        data = {}
        product_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "fetch",
            data,
            "nil",
        )
        json_product_data = json.loads(product_data)
        our_Id = create_id(json_product_data, "productId")
        product_data = {
            "productId": our_Id + 1,
            "name": name,
            "slug": slug,
            "sku": sku,
            "description": description,
            "countInStock": countInStock,
            "categoryId": categoryId,
            "image": image_name,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "insert",
            product_data,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        field = {}
        products = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(products)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "Products Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    """
    get:
    Retrieve a product

    put:
    Update a product

    delete:
    Remove a product
    """
    field = {"productId": pk}
    if request.method == "GET":
        product = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(product)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "Product Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        elif len(json_data["data"]) >= 1:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    elif request.method == "PUT":
        name = request.data["name"]
        sku = request.data["sku"]
        description = request.data["description"]
        categoryId = request.data["categoryId"]
        slug = name.replace(" ", "-")
        countInStock = request.data["countInStock"]
        vendorId = request.data["vendorId"]
        # Handle Product Image
        if "image" in request.FILES.keys():
            image = request.FILES["image"]
            product = Product(image=image, sku=sku, description=description)
            Product.save(product)
            image_name = f"media/product/{image}"
        else:
            image_name = "media/yourlogo.png"
        update_product = {
            "productId": pk,
            "categoryId": categoryId,
            "vendorId": vendorId,
            "name": name,
            "sku": sku,
            "slug": slug,
            "countInStock": countInStock,
            "description": description,
            "image": image_name,
        }
        product = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "update",
            field,
            update_product,
        )
        data = json.loads(product)
        return Response(data)
    elif request.method == "DELETE":
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1132",
            "ABCDE",
            "delete",
            field,
            "nil",
        )
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def product_in_category(request, pk, product_pk):
    field = {"categoryId": pk, "productId": product_pk}
    if request.method == "GET":
        product = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "Product",
            "Product",
            "1133",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(product)
        if len(json_data) < 1:
            return Response(
                {"message": "Product Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        elif len(json_data) >= 1:
            return Response(json_data, status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# RELATED PRODUCT ----------------------------------------------------------------------
@api_view(["GET", "POST"])
def related_product_list(request):

    field_add = {}
    if request.method == "POST":
        product_Id = request.data["product_Id"]
        relevance_score = request.data["relevance_score"]
        product_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "RelatedProduct",
            "RelatedProduct",
            "1138",
            "ABCDE",
            "insert",
            field_add,
            "nil",
        )
        json_product_data = json.loads(product_data)
        related_Id = create_id(json_product_data, "relatedId")
        field = {
            "relatedId": related_Id + 1,
            "relatedProductId": product_Id,
            "relevanceScore": relevance_score,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "RelatedProduct",
            "RelatedProduct",
            "1138",
            "ABCDE",
            "insert",
            field,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        related_products = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "RelatedProduct",
            "RelatedProduct",
            "1138",
            "ABCDE",
            "fetch",
            field_add,
            "nil",
        )
        json_data = json.loads(related_products)
        if len(json_data["data"]) < 1:
            return Response({"message": "No related Products were found"})
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# PRICING HISTORY ----------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def pricing_history_list(request):
    field_add = {}
    if request.method == "POST":
        product_Id = request.data["related_product_Id"]
        price = request.data["relevance_score"]
        started_at = request.data["started_at"]
        ended_at = request.data["ended_at"]
        pricing = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "PricingHistory",
            "PricingHistory",
            "1139",
            "ABCDE",
            "fetch",
            field_add,
            "nil",
        )
        json_pricing_data = json.loads(pricing)
        pricing_Id = create_id(json_pricing_data, "pricing_Id")
        field = {
            "pricing_Id": pricing_Id + 1,
            "product_Id": product_Id,
            "price": price,
            "started_at": started_at,
            "ended_at": ended_at,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "PricingHistory",
            "PricingHistory",
            "1139",
            "ABCDE",
            "insert",
            field,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        pricing = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "PricingHistory",
            "PricingHistory",
            "1139",
            "ABCDE",
            "fetch",
            field_add,
            "nil",
        )
        json_data = json.loads(pricing)
        if len(json_data["data"]) < 1:
            return Response({"message": "No pricing history was found"})
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
