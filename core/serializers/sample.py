# from django.db.models import fields
# from rest_framework import serializers
# from ..models.sample import Language,Programmer, Paradigm

# class LanguageSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Language
#         fields = ("id")

# class ParadigmSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta: 
#         model = Paradigm
#         fields= ("id", 'url')

# class ProgrammerSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta: 
#         model = Programmer
#         fields= ("id", 'url', 'name', 'languages')
