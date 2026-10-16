# complex datatype --------------> python native datatype ------------> json data
#                  (serialization)                        (JSONRenderer)

# ModelSerializers are used below
from rest_framework import serializers
from .models import Company, Employee

# create serializer here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"