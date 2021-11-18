from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='ProductName')
    product_stock = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'Product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
