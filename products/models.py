from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name

    class Meta():
        db_table = 'menu'



class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name


    class Meta():
        db_table = 'category' 


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)
    allergy = models.ManyToManyField('Allergy', through = 'Allergy_product')
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.korean_name


    class Meta():
        db_table = 'product'


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_name = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000, null=True)

    def __str__(self):
        return self.image_name


    class Meta():
        db_table = 'image'


class Nutrition(models.Model):
    product_name = models.CharField(max_length=45)
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.product_name


    class Meta():
        db_table = 'nutrition'


class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    def __str__(self):
        return self.name


    class Meta():
        db_table = 'allergy'


class Allergy_product(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE, blank=True)
    
    class Meta():
        db_table = 'allergy_product'

















