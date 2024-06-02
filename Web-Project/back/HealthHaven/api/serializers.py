from rest_framework import serializers
from .models import PersonalData
from .models import Post

class PersonalDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    image = serializers.ImageField()
    date_of_birth = serializers.CharField()
    blood_group = serializers.CharField()
    diagnosis = serializers.CharField()
    allergies = serializers.CharField()
    contraindications = serializers.CharField()
    guardian_contact = serializers.CharField()
    hospital = serializers.CharField()

    def create(self, validated_data):
        instance = PersonalData.objects.create(
            image = validated_data.get("image"),
            date_of_birth = validated_data.get("date_of_birth"),
            blood_group = validated_data.get("blood_group"),
            diagnosis = validated_data.get("diagnosis"),
            allergies = validated_data.get("allergies"),
            contraindications = validated_data.get("contraindications"),
            guardian_contact = validated_data.get("guardian_contact"),
            hospital = validated_data.get("hospital")
        )
        return instance

    def update(self, instance, validate_data):
        instance.image = validate_data.get("image")
        instance.date_of_birth = validate_data.get("date_of_birth")
        instance.blood_group = validate_data.get("blood_group")
        instance.diagnosis = validate_data.get("diagnosis")
        instance.allergies = validate_data.get("allergies")
        instance.contraindications = validate_data.get("contraindications")
        instance.guardian_contact = validate_data.get("guardian_contact")
        instance.hospital = validate_data.get("hospital")

        instance.save()
        return instance


class PersonalDataSerializer2(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length = 70)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PersonalData
        fields = ("id","phone_number","user_id")

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 255)
    author = serializers.CharField(max_length = 70, read_only = True)
    # user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ("id","title", "author")
