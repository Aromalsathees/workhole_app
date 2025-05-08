from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_registration_email

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the home page.")

# class GetuserContact(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetuserContact(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            send_registration_email.delay(email)  # Calling the task asynchronously
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# subjects views starts from here

class createlistSubjects(ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class createDifferentSubjects(ListCreateAPIView):
    queryset = DifferentSubjects.objects.all()
    serializer_class = DifferentSubjectsSerializer 

class createPopularSubjects(ListCreateAPIView):
    queryset = PopularSubjects.objects.all()
    serializer_class = PopularSubjectsSerializer

class createTopRelatedSubjects(ListCreateAPIView):
    queryset = ToprelatedSubjects.objects.all()
    serializer_class = ToprelatedSubjectsSerializer


class GetSubSubjects(APIView):
    def get(self, request ,id):
        queryset = DifferentSubjects.objects.filter(subject__id = id)
        serializer = DifferentSubjectsSerializer(queryset , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
  
class GetPopularRelatedSubjects(APIView):
    def get(self,request,id):
        queryset1 = PopularSubjects.objects.filter(popsub__id = id)
        queryset2 = ToprelatedSubjects.objects.filter(topsub__id = id)

        popular_serializer = PopularSubjectsSerializer(queryset1,many=True)
        related_serializer = ToprelatedSubjectsSerializer(queryset2,many=True)

        return Response({"popular_serializer":popular_serializer.data,"related_serializer":related_serializer.data},status=status.HTTP_200_OK)

class GetPopularTopRelated(APIView):
    def get(self , request, id):
        model = request.GET.get('model')
        if model == "popular":
            queryset = PopularSubjects.objects.get(id=id)
            serializer = PopularSubjectsSerializer(queryset , context={'request' : request})
            return Response(serializer.data , status=200)
        else:
            queryset = ToprelatedSubjects.objects.get(id=id)
            serializer = ToprelatedSubjectsSerializer(queryset , context={'request' : request})
            return Response(serializer.data, status=200)


class GetPopTopsearch(APIView):
    def get(self,request):
        query = request.GET.get('q','')
        pop_search = PopularSubjects.objects.filter(name__icontains=query)
        top_search = ToprelatedSubjects.objects.filter(name__icontains=query)


        pop_serializer = PopularSubjectsSerializer(pop_search,many=True)
        top_serializer = ToprelatedSubjectsSerializer(top_search,many=True)

        return Response({'pop_subjects': pop_serializer.data,'top_subjects':top_serializer.data})
    
# subjects views ends here 



# Exams views starts From Here   

class createlistExams(ListCreateAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer

class createDifferentExams(ListCreateAPIView):
    queryset = DifferentExams.objects.all()
    serializer_class = DifferentExamsSerializer 

class createPopularExams(ListCreateAPIView):
    queryset = PopularExams.objects.all()
    serializer_class = PopularExamsSerializer

class createTopRelatedExams(ListCreateAPIView):
    queryset = ToprelatedExams.objects.all()
    serializer_class = ToprelatedExamsSerializer


class GetSubExams(APIView):
    def get(self, request ,id):
        queryset = DifferentExams.objects.filter(exam__id = id)
        serializer = DifferentExamsSerializer(queryset , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetPopularRelatedExams(APIView):
    def get(self,request,id):
        queryset1 = PopularExams.objects.filter(popexam__id = id)
        queryset2 = ToprelatedExams.objects.filter(topexam__id = id)

        popular_serializer = PopularExamsSerializer(queryset1,many=True)
        related_serializer = ToprelatedExamsSerializer(queryset2,many=True)

        return Response({"popular_serializer":popular_serializer.data,"related_serializer":related_serializer.data},status=status.HTTP_200_OK) 


class GetPopularTopRelatedExams(APIView):
    def get(self , request, id):
        model = request.GET.get('model')
        if model == "popular":
            queryset = PopularExams.objects.get(id=id)
            serializer = PopularExamsSerializer(queryset , context={'request' : request})
            return Response(serializer.data , status=200)
        else:
            queryset = ToprelatedExams.objects.get(id=id)
            serializer = ToprelatedExamsSerializer(queryset , context={'request' : request})
            return Response(serializer.data, status=200)

# Exams views ends here 

# Couses views starts from here


# Exams views starts From Here   

class createlistCourses(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class createDifferentCourses(ListCreateAPIView):
    queryset = DifferentCourses.objects.all()
    serializer_class = DifferentCoursesSerializer 

class createPopularCourses(ListCreateAPIView):
    queryset = PopularCourses.objects.all()
    serializer_class = PopularCoursesSerializer

class createTopRelatedCourses(ListCreateAPIView):
    queryset = ToprelatedCourses.objects.all()
    serializer_class = ToprelatedCoursesSerializer


class GetSubCourses(APIView):
    def get(self, request ,id):
        queryset = DifferentCourses.objects.filter(course__id = id)
        serializer = DifferentCoursesSerializer(queryset , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetPopularRelatedCourses(APIView):
    def get(self,request,id):
        queryset1 = PopularCourses.objects.filter(popcourse__id = id)
        queryset2 = ToprelatedCourses.objects.filter(topecourse__id = id)

        popular_serializer = PopularCoursesSerializer(queryset1,many=True)
        related_serializer = ToprelatedCoursesSerializer(queryset2,many=True)

        return Response({"popular_serializer":popular_serializer.data,"related_serializer":related_serializer.data},status=status.HTTP_200_OK) 


class GetPopularTopRelatedCourses(APIView):
    def get(self , request, id):
        model = request.GET.get('model')
        if model == "popular":
            queryset = PopularCourses.objects.get(id=id)
            serializer = PopularCoursesSerializer(queryset , context={'request' : request})
            return Response(serializer.data , status=200)
        else:
            queryset = ToprelatedCourses.objects.get(id=id)
            serializer = ToprelatedCoursesSerializer(queryset , context={'request' : request})
            return Response(serializer.data, status=200)

        
