import json
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from product.dowellconnection1 import dowellconnection
from product.create_id import create_id


error_500_message = {"message": "Error processing your request, Retry"}
# CATEGORY ----------------------------------------------------------------------
@api_view(["GET", "POST"])
def category_list(request):
    """
    get:
    Category List

    post:
    Create a new category

    parameters:
    name: string
    description: string
    """
    if request.method == "POST":
        name = request.data["name"]
        description = request.data["description"]
        test_data = {}
        category_data = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
            "1133",
            "ABCDE",
            "fetch",
            test_data,
            "nil",
        )
        json_category_data = json.loads(category_data)
        cat_Id = create_id(json_category_data, "categoryId")
        category_data = {
            "name": name,
            "categoryId": cat_Id + 1,
            "description": description,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
            "1133",
            "ABCDE",
            "insert",
            category_data,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        field = {}
        categories = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
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


@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    field = {"categoryId": int(pk)}
    if request.method == "GET":
        category = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
            "1133",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(category)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "The Category Requested is unavailable"},
                status=status.HTTP_404_NOT_FOUND,
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    elif request.method == "PUT":
        name = request.data["name"]
        description = request.data["description"]
        update_category = {
            "name": name,
            "categoryId": pk,
            "description": description,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
            "1133",
            "ABCDE",
            "update",
            field,
            update_category,
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "ProductCategory",
            "ProductCategory",
            "1133",
            "ABCDE",
            "delete",
            field,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# SUB CATEGORY -------------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def sub_category_list(request):
    """
    This API endpoint allows creation and listing of sub-Categories.

    """
    if request.method == "POST":
        name = request.data["name"]
        categoryId = request.data["categoryId"]
        description = request.data["description"]

        sub_cat_field = {}

        sub_categories = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "fetch",
            sub_cat_field,
            "nil",
        )
        json_sub_cat_data = json.loads(sub_categories)

        sub_cat_Id = create_id(json_sub_cat_data, "subCategoryId")

        sub_category_data = {
            "name": name,
            "subCategoryId": sub_cat_Id + 1,
            "description": description,
            "categoryId": categoryId,
        }
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "insert",
            sub_category_data,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data_field = {}
        sub_categories = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "fetch",
            data_field,
            "nil",
        )
        json_data = json.loads(sub_categories)
        if len(json_data["data"]) < 1:

            return Response(
                {"message": "No Sub Categories found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["GET", "PUT", "DELETE"])
def sub_category_detail(request, pk):
    """
    get:
    Read a sub category

    put:
    Update a sub category

    """
    field = {"subCategoryId": pk}
    if request.method == "GET":
        category = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "fetch",
            field,
            "nil",
        )
        json_data = json.loads(category)
        if len(json_data["data"]) < 1:
            return Response(
                {"message": "No Sub Category  Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        elif len(json_data["data"]) >= 1:
            return Response(json_data["data"], status=status.HTTP_200_OK)
        else:
            return Response(
                error_500_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    elif request.method == "PUT":
        sub_name = request.data["name"]
        categoryId = request.data["categoryId"]
        description = request.data["description"]
        update_sub_category = {
            "name": sub_name,
            "categoryId": categoryId,
            "subCategoryId": pk,
            "description": description,
        }
        sub_category = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "update",
            field,
            update_sub_category,
        )
        data = json.loads(sub_category)
        return Response(data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        res = dowellconnection(
            "dowellstores",
            "bangalore",
            "dowellstores",
            "SubCategory",
            "SubCategory",
            "1134",
            "ABCDE",
            "delete",
            field,
            "nil",
        )
        data = json.loads(res)
        return Response(data, status=status.HTTP_204_NO_CONTENT)
