from django.db import models
from main.models import Product  # 절대 경로를 사용하여 main 앱의 Product 모델을 import

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, verbose_name='리뷰 아이디')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, db_index=True, verbose_name='제품')
    reviews = models.CharField(max_length=500, verbose_name='리뷰 내용')

    class Meta:
        db_table = 'reviews'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰들'

    def __str__(self):
        return f"{self.product.product_id} - 리뷰 {self.review_id}"