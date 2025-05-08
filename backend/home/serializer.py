from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = '__all__'

# Subjects serilizers starts from here
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class DifferentSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DifferentSubjects
        fields = '__all__'       

class PopularSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularSubjects
        fields = '__all__'     

class ToprelatedSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToprelatedSubjects
        fields = '__all__'   

# subjects serilizers ends here   


# Exams serilizers starts from here   

class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = '__all__'

class DifferentExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DifferentExams
        fields = '__all__'       

class PopularExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularExams
        fields = '__all__'     

class ToprelatedExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToprelatedExams
        fields = '__all__'   

# Exams serilizers Ends here   


# courses serilizers starts from here   

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = '__all__'

class DifferentCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DifferentCourses
        fields = '__all__'       

class PopularCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularCourses
        fields = '__all__'     

class ToprelatedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToprelatedCourses
        fields = '__all__'   
  

# Exams serilizers Ends here   


    


    