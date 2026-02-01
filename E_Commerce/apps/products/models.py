from django.db import models
from apps.categories.models import Category
import uuid
from uuid import uuid4


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_stock = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'category_id'], name='unique_product_name_per_category'),
            models.Index(fields=['category_id'], name='idx_category_id'),
            models.Index(fields=['price'], name='price_idx'),
            models.indexes.Index(fields=['created_at'], name='created_at_brin_idx'),
            models.indexes.Index(fields=['updated_at'], name='updated_at_brin_idx'),
            models.CheckConstraint(check=models.Q(price__gte=0), name='price_non_negative'),
        ]
        
    def __str__(self):
        return self.name

# Create your models here.
