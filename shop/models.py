from MySQLdb import Timestamp
from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self) -> str:
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    phone = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=111, default="")

    def __str__(self) -> str:
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=111, default="")
    address = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111, default="")
    state = models.CharField(max_length=111, default="")
    zip_code = models.CharField(max_length=111, default="")
    phone = models.CharField(max_length=50, default="")

    def __str__(self) -> str:
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.update_desc[0:7] + "...."
