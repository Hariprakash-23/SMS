from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from students.models import Student
from courses.models import Course
from attendance.models import Attendance
from marks.models import Marks
from .serializers import (
    UserSerializer, StudentSerializer, CourseSerializer,
    AttendanceSerializer, MarkSerializer
)

#protecting api view - (Imp: Response)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['GET'])
@permission_classes([IsAuthenticated])

def dashboard_api(request): 
    """Simply if you hit http://127.0.0.1:8000/api/dashboard/ it gives error 
    In Postman: Authorization: Bearer: put Your_access_token and hit now it works
    """
    return Response({
        'message': 'JWT Protected API Working',
        'user': request.user.username
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer