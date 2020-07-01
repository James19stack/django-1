from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length = 30, blank = True)

    def __str__(self):
        return self.category
    def save_category(self):
        self.save()  
    @classmethod
    def update_category(cls,name,update):
        Category.objects.filter(category=name).update(category=update)
        update=Category.objects.get(category=update)
        return update   
    

    @classmethod    
    def delete_category(cls,category):
        Category.objects.get(category=category).delete()

class Location(models.Model):
    location = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return self.location   
    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls,name,update):
        Location.objects.filter(location=name).update(location=update)  
        updated=Location.objects.get(location=update)
        return updated
        
      
    @classmethod    
    def delete_location(cls,location):
        deleted=Location.objects.get(location=location).delete()
        return deleted     

class Image(models.Model):
    
    name = models.CharField(max_length = 30, blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog/', blank = True)
    category = models.ForeignKey('Category',on_delete = models.CASCADE,null =True)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)            

    def __str__(self):
        return self.name


    def save_name(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        fine = cls.objects.filter(category__category__icontains=search_term)
        return fine    
        