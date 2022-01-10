# from django.db import models

# class Paradigm(models.Model):
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name

# class Language (models.Model):
#     name = models.CharField(max_length=255)
#     paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE) # one to one with patadigm 

#     def __str__(self):
#         return self.name


# class Programmer(models.Model):
#     name= models.CharField(max_length=255)
#     language = models.ManyToManyField(Language)

#     def __str__(self):
#         return self.name

