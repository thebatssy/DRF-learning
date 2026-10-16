from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    #companies/{companyId}/employees/
    @action(detail=True, methods=['get'])
    def employees(self, req, pk=None):
        try:
            comp = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=comp)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request':req})
            return Response(emps_serializer.data)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=404)
            
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
