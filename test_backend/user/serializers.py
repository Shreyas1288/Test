from rest_framework import serializers
from user.models import Dataset



class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Dataset
        fields = ['id','yop', 'sp', 'dist', 'owners', 'fuel', 'owner_type', 'transmission']





#------------below is the method one----------------------------
# class DatasetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     yop = serializers.IntegerField()
#     sp = serializers.IntegerField()    
#     dist = serializers.IntegerField()    
#     owners = serializers.IntegerField()    
#     fuel = serializers.CharField(max_length=20,default = 'petrol')
#     owner_type = serializers.CharField(max_length = 20,default='individual')
#     transmission = serializers.CharField(max_length = 20,default = 'manual')

#     def create(self, validated_data):
#         return Dataset.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.yop = validated_data.get('yop', instance.yop)
#         instance.sp  = validated_data.get('sp', instance.sp)
#         instance.dist = validated_data.get('dist', instance.dist)
#         instance.owners = validated_data.get('owners', instance.owners)
#         instance.fuel = validated_data.get('fuel' , instance.fuel)
#         instance.owner_type = validated_data.get('owner_type', instance.owner_type)
#         instance.transmission = validated_data.get('transmission', instance.transmission)
#         instance.save()
#         return instance

