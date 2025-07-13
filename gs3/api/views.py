from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt #this is used to exempt the view from CSRF verification, this is useful for API views where CSRF token is not required
def student_api(request):
    if request.method == 'GET': # GET method
        # Get the JSON data from the request body
        json_data = request.body #the raw body of the request which contains the json data sent by the client
        stream = io.BytesIO(json_data) #converts the raw body which is in bytes into a stream so it can be parsed
        pythondata = JSONParser().parse(stream) #parse the stream into python data like dictionary
        id = pythondata.get('id', None) #this tries to get the id key from the parsed data, it id is not provided, it defaults to none
        if id is not None:
            stu = Student.objects.get(id=id) #fetch the student object with that specific id 
            serializer = StudentSerializer(stu) # converts the student object into a json format(serializes it)
            json_data = JSONRenderer().render(serializer.data) #take the serialized data and convert it into json format
            return HttpResponse(json_data, content_type='application/json') # returns the json data as a response
        #if id is not provided, it means we want to fetch all the students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True) #many=True means we are serializing multiple objects
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json') #returns the json data as a response
    
    if request.method == 'POST': # POST method
        json_data = request.body #the raw body of the request which contains the json data sent by the client
        stream = io.BytesIO(json_data) #converts the raw body which is in bytes into a stream so it can be parsed
        pythondata = JSONParser().parse(stream) #parse the stream into python data like dictionary
        serializer = StudentSerializer(data=pythondata) #serializer is used to validate and save the data
        if serializer.is_valid(): #check if the data is valid
            serializer.save() #save the data into the database
            res = {'msg': 'Data Created'} #this is a response message
            json_data = JSONRenderer().render(res) #convert the response message into json format
            return HttpResponse(json_data, content_type='application/json') #returns the json data as a response
        json_data = JSONRenderer().render(serializer.errors) #convert the errors into json format
        return HttpResponse(json_data, content_type='application/json') #returns the json data as a response
    
    if request.method == 'PUT': # PUT method
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True) #partial=True means we are updating only the provided fields
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    
        