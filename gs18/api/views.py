from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

#just this much of the code is needed to create a crud application
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    