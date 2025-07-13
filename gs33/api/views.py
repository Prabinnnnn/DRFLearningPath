from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #returning all the students passed by the user who is currently logged in
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user) #this user will be the one who is logged in currently

