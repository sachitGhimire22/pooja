from django.db import models


# Create your models here.


class Person(models.Model):
    first_name = models.CharField (max_length=50,null=False,default='first')
    lastName = models.CharField(max_length=30,null=False,default="last")
    username =  models.CharField(max_length=30,null=False,default="user")
    password = models.CharField(max_length=40)
    email = models.EmailField(null=True)

    
    

class Collection(models.Model):
    collection_name = models.CharField(max_length=100,null=False)
    collection_price = models.IntegerField(null=False)
    collection_image = models.ImageField(null=False,upload_to='media/pooja_app/images/collections/')
    def __str__(self):
        return self.collection_name
    
    
class Item (models.Model):
    item_name = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image  = models.ImageField(null=False, upload_to='media/pooja_app/images/items/')
    category_id = models.ForeignKey(Collection,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.item_name