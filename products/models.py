from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    display_category = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    main_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    display_category = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub-categories'


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    preview_text = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='uploads/product_thumbnails',
                                  default='uploads/product_thumbnails/default.jpg')

    def __str__(self):
        return self.title
