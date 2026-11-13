from rest_framework import serializers
from .models import Student

# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name must start with R")
    
class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    #name = serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        #fields = '__all__'
        #read_only_fields = ['name', 'roll']
        #extra_kwargs = {'name': {'read_only': True}}
        
    # Field level validation
    # def validate_roll(self, value):
    #     if value > 200:
    #         raise serializers.ValidationError("Seat Full")
    #     return value
    
    # Object level validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
    #         raise serializers.ValidationError("Rohit must be from Ranchi")
    #     return data