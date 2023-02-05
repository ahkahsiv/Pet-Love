from rest_framework import serializers
from . models import *


class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class  AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalBreed
        fields=["animal_breed"]

class  AnimalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalColor
        fields=["animal_color"]
        # Earlier created and updated also got serialized, now only animal color is serialized., same eith breed.

class  AnimalSerializer(serializers.ModelSerializer):
    animal_color=AnimalColorSerializer(many=True)
    animal_breed=AnimalBreedSerializer(many=True)
    animal_category=CategorySerializer()

        # def to_representation(self, instance):
        #     animal_color=AnimalColorSerializer(many=True)
        #     animal_breed=AnimalBreedSerializer(many=True)

        # payload ={
        #     'animal_category':instance.animal_category.category_name,
        #     'animal_likes':instance.animal_likes,
        #     'animal_name':instance.animal_name,
        #     'animal_views':instance.animal_views,
        #     'animal_description':instance.animal_description,
        #     'animal_color':animal_color_serializer.data,
        #     'animal_breed':animal_breed_serializer.data,
        # }
        # return payload
    class Meta:
        model=Animal
        exclude=['updated_at']

class  AnimalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalLocation
        fields="__all__"

class  AnimalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnimalImages
        fields="__all__"
