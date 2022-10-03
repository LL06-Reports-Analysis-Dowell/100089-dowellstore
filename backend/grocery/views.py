import base64
import json
from PIL import Image
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .dowellconnection1 import dowellconnection
from .models import Product


def api_home(request):
    return JsonResponse(
        {
            "message": "The API Endpoint is Up"
        }
    )


@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({
        "Message": "API decorators"
    })


# PRODUCT --------------------------------------------------

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'POST':
        name = request.data['name']
        sku = request.data['sku']
        description = request.data['description']
        price = request.data['price']
        category_id = request.data['category_id']

        # Handle Product Image
        if 'image' in request.FILES.keys():
            image = request.FILES['image']
            product = Product(image=image, sku=sku, description=description, price=price)
            Product.save(product)
            # Convert Image to base64
            # TODO: Fix Some Test Failing: If the Image name has spaces
            # with open(f"media/product_images/{image}", "rb") as our_image:
            #     # print(our_image)
            #     converted_string = base64.b64encode(our_image.read())
            #     print(converted_string.decode('utf-8'))

        data = {}
        product_data = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132",
                                        "ABCDE",
                                        "fetch", data, "nil")
        json_product_data = json.loads(product_data)

        prod = []
        # Check if
        if len(json_product_data["data"]) >= 1:
            for i in json_product_data["data"]:
                if "product_id" in i:
                    prod.append(i["product_id"])
        our_id = max(prod)

        product_data = {
            "name": name,
            "sku": sku,
            "description": description,
            "price": price,
            "product_id": our_id + 1,
            "category_id": category_id,
            "image": converted_string.decode('utf-8')
        }
        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132", "ABCDE",
                               "insert", product_data, "nil")
        print(res)
        return Response(product_data, status=status.HTTP_201_CREATED)
    else:
        field = {}
        products = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132", "ABCDE",
                                    "fetch", field, "nil")
        # TODO: Fix Error fetching the products over a browsable API
        data = json.loads(products)
        return Response(data["data"], status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    field = {
        "product_id": pk
    }
    if request.method == 'GET':

        product = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132", "ABCDE",
                                   "fetch", field, "nil")
        data = json.loads(product)
        data1 = data["data"]
        print(data1)
        return Response(data["data"])

    elif request.method == 'PUT':
        name = request.data['name']
        sku = request.data['sku']
        description = request.data['description']
        price = request.data['price']
        category_id = request.data['category_id']
        image = request.data['image']

        update_product = {
            "product_id": pk,
            "category_id": category_id,
            "name": name,
            "sku": sku,
            "description": description,
            "price": price,
            "image": image
        }

        product = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132", "ABCDE",
                                   "update", field, update_product)
        data = json.loads(product)
        return Response(data)

    elif request.method == 'DELETE':
        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "Product", "Product", "1132", "ABCDE",
                               "delete", field, "nil")
        data = json.loads(res)
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# CATEGORY ----------------------------------------------------------------------

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'POST':
        name = request.data["name"]
        code = request.data["code"]
        description = request.data["description"]

        test_data = {}
        category_data = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory",
                                         "ProductCategory",
                                         "1133", "ABCDE", "fetch", test_data, "nil")
        json_category_data = json.loads(category_data)

        prod = []
        # Check if
        if len(json_category_data["data"]) >= 1:
            for i in json_category_data["data"]:
                if "category_id" in i:
                    prod.append(i["category_id"])
        cat_id = max(prod)

        category_data = {
            "name": name,
            "code": code,
            "category_id": cat_id + 1,
            "description": description,
        }

        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory", "ProductCategory",
                               "1133", "ABCDE", "insert", category_data, "nil")
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)

    else:
        field = {}
        categories = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory", "ProductCategory",
                                      "1133", "ABCDE", "fetch", field, "nil")
        data = json.loads(categories)
        return Response(data["data"])


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    field = {
        "category_id": pk
    }
    if request.method == 'GET':
        category = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory", "ProductCategory",
                                    "1133", "ABCDE", "fetch", field, "nil")
        data = json.loads(category)
        return Response(data["data"])

    elif request.method == 'PUT':
        name = request.data["name"]
        code = request.data["code"]
        description = request.data["description"]

        update_category = {
            "name": name,
            "code": code,
            "category_id": pk,
            "description": description,
        }

        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory", "ProductCategory",
                               "1133", "ABCDE", "update", field, update_category)
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "ProductCategory", "ProductCategory",
                               "1133", "ABCDE", "delete", field, "nil")
        data = json.loads(res)
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# SUB CATEGORY -------------------------------------------------------------------

@api_view(['GET', 'POST'])
def sub_category_list(request):
    if request.method == 'POST':
        name = request.data["name"]
        code = request.data["code"]
        description = request.data["description"]
        parent_code = request.data["parent_code"]

        sub_cat_field = {}

        sub_categories = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory",
                                          "1134",
                                          "ABCDE", "fetch", sub_cat_field, "nil")
        json_sub_cat_data = json.loads(sub_categories)

        prod = []
        # Check if
        if len(json_sub_cat_data["data"]) >= 1:
            for i in json_sub_cat_data["data"]:
                if "sub_category_id" in i:
                    prod.append(i["sub_category_id"])
        sub_cat_id = max(prod)

        sub_category_data = {
            "name": name,
            "code": code,
            "sub_category_id": sub_cat_id + 1,
            "description": description,
            "parent_code": parent_code
        }

        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory",
                               "1134", "ABCDE", "insert", sub_category_data, "nil")
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data_field = {}
        sub_categories = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory",
                                          "1134",
                                          "ABCDE", "fetch", data_field, "nil")
        data = json.loads(sub_categories)
        return Response(data["data"])


@api_view(['GET', 'PUT', 'DELETE'])
def sub_category_detail(request, pk):
    field = {
        "sub_category_id": pk
    }
    if request.method == 'GET':
        category = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory", "1134",
                                    "ABCDE", "fetch", field, "nil")
        data = json.loads(category)
        return Response(data["data"])

    elif request.method == 'PUT':
        sub_name = request.data["name"]
        code = request.data["code"]
        description = request.data["description"]
        parent_code = request.data["parent_code"]

        update_sub_category = {
            "name": sub_name,
            "code": code,
            "sub_category_id": pk,
            "description": description,
            "parent_code": parent_code
        }

        sub_category = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory",
                                        "1134",
                                        "ABCDE", "update", field, update_sub_category)
        data = json.loads(sub_category)
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        res = dowellconnection("dowellstores", "bangalore", "dowellstores", "SubCategory", "SubCategory", "1134",
                               "ABCDE", "delete", field, "nil")
        data = json.loads(res)
        return Response(data, status=status.HTTP_204_NO_CONTENT)
