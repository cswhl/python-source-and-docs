from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmpolyeeApp.models import Departments, Employees
from EmpolyeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
# @csrf_exempt将视图函数标记为不受CSRF保护
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        # 将模型实例转换为python原生数据类型
        department_serializer = DepartmentSerializer(departments, many=True)
        # 转换为JSON数据并返回给前端
        return JsonResponse(department_serializer.data, safe=False)

    if request.method == 'POST':
        # 将request请求转为dict
        department_data = JSONParser().parse(request)
        print(department_data)
        # 反序列化
        department_serializer = DepartmentSerializer(data=department_data)
        print(department_serializer)
        #  反序列化数据为模型实例并验证传给data参数的数据
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    if request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    if request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete Succefully!!", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    if request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    if request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Succefully!!", safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['uploadFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
