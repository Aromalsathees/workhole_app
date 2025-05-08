from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-user-details',GetuserContact.as_view(),name='add_user_details'),

    # subjects urls starts from here
    path('createlistSubjects',createlistSubjects.as_view(),name='createlistSubjects'),
    path('createDifferentSubjects',createDifferentSubjects.as_view(),name='createDifferentSubjects'),
    path('createPopularSubjects',createPopularSubjects.as_view(),name='createPopularSubjects'),
    path('createTopRelatedSubjects',createTopRelatedSubjects.as_view(),name='createTopRelatedSubjects'),
    path('GetSubSubjects/<int:id>/',GetSubSubjects.as_view()),
    path('GetPopularRelatedSubjects/<int:id>/',GetPopularRelatedSubjects.as_view()),
    path('get-material-resources/<id>/' , GetPopularTopRelated.as_view()),
    path('get-top-pop-search/',GetPopTopsearch.as_view()),
    # subjects urls Ends here

    # Exams urls starts from here

    path('createlistExams',createlistExams.as_view(),name='createlistExams'),
    path('createDifferentExams',createDifferentExams.as_view(),name='createDifferentExams'),
    path('createPopularExams',createPopularExams.as_view(),name='createPopularExams'),
    path('createTopRelatedExams',createTopRelatedExams.as_view(),name='createTopRelatedExams'),
    path('GetSubExams/<int:id>/',GetSubExams.as_view()),
    path('GetPopularRelatedExams/<int:id>/',GetPopularRelatedExams.as_view()),
    path('get-material-exams/<id>/',GetPopularTopRelatedExams.as_view()),

    # Exams urls ends from here

    # Courses urls starts from here
    
    path('createlistCourses',createlistCourses.as_view(),name='createlistCourses'),
    path('createDifferentCourses',createDifferentCourses.as_view(),name='createDifferentCourses'),
    path('createPopularCourses',createPopularCourses.as_view(),name='createPopularCourses'),
    path('createTopRelatedCourses',createTopRelatedCourses.as_view(),name='createTopRelatedCourses'),
    path('GetSubCourses/<int:id>/',GetSubCourses.as_view()),
    path('GetPopularRelatedCourses/<int:id>/',GetPopularRelatedCourses.as_view()),
    path('get-material-courses/<id>/',GetPopularTopRelatedCourses.as_view()),

    
]
