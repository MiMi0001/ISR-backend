import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .models import Product


def index(request):
    products = Product.objects.select_related('tax_category').all
    template = loader.get_template("products/products_list.html")
    context = {"products": products}

    return HttpResponse(template.render(context, request))


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_all(request):
    payload = json.loads(request.body)
    orderby = payload["orderby"]
    asc_desc = "-" if payload["ascdesc"] == "DESC" else ""
    print(f'order by: {asc_desc + orderby}')
    products = list(Product.objects.select_related('tax_category').order_by(asc_desc + orderby).values())
    # data = serialize("json", products)

    return JsonResponse(products, safe=False)
