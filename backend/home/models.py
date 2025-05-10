from django.db import models


class UserContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    pname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    wnumber = models.CharField(max_length=15)
    pnumber = models.CharField(max_length=15)
    cmode = models.CharField(
        max_length=10,
        choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Hybrid', 'Hybrid')],
        default='Online'
    )

    def __str__(self):
        return self.name
    

# subjetcs models starts from here 
class Subjects(models.Model):
    name =  models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class DifferentSubjects(models.Model):
    
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="")
   

    def __str__(self):
        return self.name


class PopularSubjects(models.Model):
    
   MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
   popsub = models.ForeignKey(DifferentSubjects,on_delete=models.CASCADE)
   name = models.CharField(max_length=50,default="")
   image = models.FileField(upload_to='images/',null=True, blank=True)
   videos = models.FileField(upload_to='images/',null=True,blank=True)
   pdf = models.FileField(upload_to='images/',null=True,blank=True)
   notes = models.FileField(upload_to='images',null=True,blank=True)

    
   def __str__(self):
        return self.name


class ToprelatedSubjects(models.Model):
      
    MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
    
    topsub = models.ForeignKey(DifferentSubjects,on_delete=models.CASCADE)   
    name = models.CharField(max_length=50,default="")
    image = models.FileField(upload_to='images/',null=True, blank=True)
    videos = models.FileField(upload_to='images/',null=True,blank=True)
    pdf = models.FileField(upload_to='images/',null=True,blank=True)
    notes = models.FileField(upload_to='images',null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
class Downloadmaterials(models.Model):
    pop_subject = models.ForeignKey(PopularSubjects,on_delete=models.CASCADE)
    top_subject = models.ForeignKey(ToprelatedSubjects,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank=True)    

# subjetcs models Ends here



# Exams models starts from here 
class Exams(models.Model):
    name =  models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class DifferentExams(models.Model):
    
    exam = models.ForeignKey(Exams,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="")
   

    def __str__(self):
        return self.name


class PopularExams(models.Model):
    
   MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
   popexam = models.ForeignKey(DifferentExams,on_delete=models.CASCADE)
   name = models.CharField(max_length=50,default="")
   image = models.FileField(upload_to='images/',null=True, blank=True)
   videos = models.FileField(upload_to='images/',null=True,blank=True)
   pdf = models.FileField(upload_to='images/',null=True,blank=True)
   notes = models.FileField(upload_to='images',null=True,blank=True)

    
   def __str__(self):
        return self.name


class ToprelatedExams(models.Model):
      
    MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
    
    topexam = models.ForeignKey(DifferentExams,on_delete=models.CASCADE)   
    name = models.CharField(max_length=50,default="")
    image = models.FileField(upload_to='images/',null=True, blank=True)
    videos = models.FileField(upload_to='images/',null=True,blank=True)
    pdf = models.FileField(upload_to='images/',null=True,blank=True)
    notes = models.FileField(upload_to='images',null=True,blank=True)
    
    
    def __str__(self):
        return self.name

# Exams models ends here




# Courses models starts from here

class Courses(models.Model):
    name =  models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class DifferentCourses(models.Model):
    
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="")
   

    def __str__(self):
        return self.name


class PopularCourses(models.Model):
    
   MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
   popcourse = models.ForeignKey(DifferentCourses,on_delete=models.CASCADE)
   name = models.CharField(max_length=50,default="")
   image = models.FileField(upload_to='images/',null=True, blank=True)
   videos = models.FileField(upload_to='images/',null=True,blank=True)
   pdf = models.FileField(upload_to='images/',null=True,blank=True)
   notes = models.FileField(upload_to='images',null=True,blank=True)

    
   def __str__(self):
        return self.name


class ToprelatedCourses(models.Model):
      
    MATERIAL_TYPES = [
       ('pdf','PDF'),
       ('image','IMAGE'),
       ('video','VIDEO'),
   ]
    
    topecourse = models.ForeignKey(DifferentCourses,on_delete=models.CASCADE)   
    name = models.CharField(max_length=50,default="")
    image = models.FileField(upload_to='images/',null=True, blank=True)
    videos = models.FileField(upload_to='images/',null=True,blank=True)
    pdf = models.FileField(upload_to='images/',null=True,blank=True)
    notes = models.FileField(upload_to='images',null=True,blank=True)
    
    
    def __str__(self):
        return self.name

#  courses models ends here   


