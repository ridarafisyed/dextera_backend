from django.db import models

class Profile(models.Model):
    # profile
    f_name= models.CharField(max_length=255, default="", blank=True)
    m_name= models.CharField(max_length=255, default="", blank=True)
    l_name= models.CharField(max_length=255, default="", blank=True)
    p_email= models.EmailField(max_length=255, default="")
    role= models.CharField(max_length=255, default="", blank=True)
    email= models.EmailField(max_length=255, default="")
    mobile = models.IntegerField(default=0, blank=True, null=True)
    phone = models.IntegerField(default=0, blank=True, null=True)
    state = models.CharField(max_length=255, default="", blank=True)
    city = models.CharField(max_length=255, default="", blank=True)
    language = models.CharField(max_length=255, default="", blank=True)
    locate = models.BooleanField(default=False)
    search_active = models.BooleanField(default=False)
    
    # education 
    law_school = models.CharField(max_length=255, default="", blank=True)
    grad_year = models.IntegerField(default=0)
    bar_admit_date = models.CharField(max_length=255, default="", blank=True)
    undergrad_school = models.CharField(max_length=255, default="", blank=True)
    undergrad_area = models.CharField(max_length=255, default="", blank=True)
    undergrad_year = models.CharField(max_length=255, default="", blank=True)
    bar_no =  models.IntegerField(default=12345678, blank=True)
    admitted_practice = models.CharField(max_length=255, default="", blank=True)
    
    # work history
    practice_time = models.CharField(max_length=255, default="", blank=True)
    longest_tenure = models.CharField(max_length=255, default="", blank=True)
    average_tenure = models.CharField(max_length=255, default="", blank=True)
    current_tenure = models.CharField(max_length=255, default="", blank=True)
    past_bar_companies_no = models.CharField(max_length=255, default="", blank=True)
    primary_area = models.CharField(max_length=255, default="", blank=True)

    status = models.CharField(max_length=255, default="")

    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Member(models.Model):
    f_name= models.CharField(max_length=255, default="", blank=True)
    m_name= models.CharField(max_length=255, default="", blank=True)
    l_name= models.CharField(max_length=255, default="", blank=True)
    p_email= models.EmailField(max_length=255, default="")
    role= models.CharField(max_length=255, default="", blank=True)
    c_email= models.EmailField(max_length=255, default="")
    rate= models.IntegerField(default=0, blank=True, null=True)
    time_zone= models.CharField(max_length=255, default="", blank=True)
    group= models.CharField(max_length=255, default="", blank=True)
    job_title= models.CharField(max_length=255, default="", blank=True)
    bar_no= models.CharField(max_length=255, default="", blank=True)
    street= models.CharField(max_length=255, default="", blank=True)
    suite= models.CharField(max_length=255, default="", blank=True)
    city= models.CharField(max_length=255, default="", blank=True)
    state= models.CharField(max_length=255, default="", blank=True)
    zip =models.CharField(max_length=255, default="", blank=True)
    ext=  models.CharField(max_length=255, default="", blank=True)
    mobile= models.CharField(max_length=255, default="", blank=True)
    home= models.CharField(max_length=255, default="", blank=True)
    work_no= models.CharField(max_length=255, default="", blank=True)
    phone_ext= models.CharField(max_length=255, default="", blank=True)


class Group(models.Model):
    name = models.CharField(max_length=250, unique=True)
    
    def __str__(self):
        return self.name


# class Task(models.Model):
#     date = models.CharField(max_length=250, unique=True)
#     time = models.CharField(max_length=250, unique=True)
#     user = models.CharField(max_length=250, unique=True)
#     task = models.CharField(max_length=250, unique=True)
#     status = models.CharField(max_length=250, unique=True)

