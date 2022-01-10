
from django.db import models
from rest_framework import serializers
from ..models.profile import Member, Profile, Role, Group

class UserRoleSerializer(serializers.ModelSerializer):
  class Meta:
    models = Role
    fields = '__all__'

class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ('id',
        'user',
                    'first_name',
                    'last_name',
                    'role',
                    'email',
                   )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ('id',
                    'username',
                    'email',
                    'mobile',
                    'phone',
                    'state',
                    'city',
                    'language',
                    'locate',
                    'search_active',
                    'law_school',
                    'grad_year',
                    'bar_admit_date',
                    'undergrad_school',
                    'undergrad_area',
                    'undergrad_year',
                    'bar_no',
                    'admitted_practice',
                    'practice_time',
                    'longest_tenure',
                    'average_tenure',
                    'current_tenure',
                    'past_bar_companies_no',
                    'primary_area',)

class CreateMamberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields =  (
            "f_name",
            "m_name",
            "l_name",
            "c_email",
            "rate",
            "role",
            "time_zone",
            "group",
            "job_title",
            "bar_no",
            "street",
            "suite",
            "city",
            "state",
            "zip",
            "ext",
            "mobile",
            "home",
            "work_no",
            "p_email",
            "phone_ext",
        )
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields =  (
            "id",
            "name"
        )
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =  (
            "id",
            "name"
        )