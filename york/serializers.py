from rest_framework import serializers

from .models import PuppyInfo

class PuppyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuppyInfo
        fields = '__all__'

class CreatePuppyInfoSerializer(serializers.ModelSerializer):
    # age = SerializerMethodField()
    class Meta:
        model = PuppyInfo
        fields = '__all__'

    def update(self, instance, validated_data ):
        instance.age = validated_data.get('age', instance.age) * 10
        instance.save()
        return instance


# class CreatePuppyInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=20, required=False, allow_blank=True)
#     sex = serializers.CharField(max_length=6, required=False, allow_blank=True)
#     age = serializers.CharField(max_length=2, required=False, allow_blank=True)
#     description = serializers.TextField(max_length=2000, required=False, allow_blank=True)
    
#     def create(self, validated_data):
#         return PuppyInfo.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
#         """
#         instance.profile_image = validated_data.get('profile_image', instance.profile_image)
#         instance.name = validated_data.get('name', instance.name)
#         instance.sex = validated_data.get('sex', instance.sex) * 10
#         instance.age = validated_data.get('age', instance.age)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
    # def to_representation(self, obj):
    #     return {
    #         'age': get_age()
    #     }

    # def update(self, validated_data):
    #     return PuppyInfo.objects.update(**validated_data)
    # def get_age(self, obj):
    #     obj.age = self.age * 10
    #     return str(obj.age)
        # def to_representation(self, obj):
        #     data = super(CreatePuppyInfoSerializer, self).to_representation(obj)
        #     data['age'] = self.mask_ssn(data['ssn'])
        #     return data


            # self.age = int(self.age) * 10
            # serializer.save()
            # super(PuppyInfo, self).save(obj, *args, **kwargs)