from rest_framework.views import APIView
from . serializers import JobSerializer, UserSerializer, ApplicationSerializer
from rest_framework.response import Response
from . models import Job,User,Application
from rest_framework import status

class JobList(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class ApplicationList(APIView):
    def get(self, request):
        app = Application.objects.all()
        serializer = ApplicationSerializer(app,many=True)
        return Response(serializer.data)
class JobCreate(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors,status=400)
class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

