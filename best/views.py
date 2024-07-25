from django.shortcuts import get_object_or_404, render

from main.models import DiseaseCategory, Product


# Create your views here.

def best_product(request):
    best_product = Product.objects.all().order_by("-protein")
    return render(request, 'best/best_product.html', {'productList' : best_product})
from django.shortcuts import render
from django.db.models import Count
from .models import Review
from main.models import Product


# Create your views here.

# def best_product(request):
#     best_product = Product.objects.all().order_by("-protein")
#     return render(request, 'best/best_product.html', {'productList' : best_product})
def best_product(request):

    disease_categories = DiseaseCategory.objects.all()
    top_products_by_category = {}

    for category in disease_categories:
        top_products = Review.objects.filter(product__dcate=category).values('product_id').annotate(total_reviews=Count('product_id')).order_by('-total_reviews')[:5]
        top_product_ids = [product['product_id'] for product in top_products]
        top_products_details = Product.objects.filter(product_id__in=top_product_ids)
        top_products_by_category[category.dcate_id] = top_products_details


 # 현재 첫화면에서 전체 순위를 보여주기 때문에  전체 상품 TOP5을 가져오기 위한 부분
    overall_top_products = Review.objects.values('product_id').annotate(total_reviews=Count('product_id')).order_by('-total_reviews')[:5]
    overall_top_product_ids = [product['product_id'] for product in overall_top_products]
    overall_top_products_details = Product.objects.filter(product_id__in=overall_top_product_ids)

    return render(request, "best/best_product.html", {
        'all_products': overall_top_products_details,
        'top_products_by_category': top_products_by_category,
        'disease_categories': disease_categories,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    return render(request, 'best/product_detail.html', {'product': product})