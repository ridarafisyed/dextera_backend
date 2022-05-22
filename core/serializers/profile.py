from rest_framework import serializers
from ..models.profile import Member, Profile, Group
from django.contrib.auth import get_user_model
 
User = get_user_model()


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
            "id",
            "f_name",
            "m_name",
            "l_name",
            "p_email",
            "role",
            "c_email",
            "rate",
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
            "phone_ext",
        )
        def create(self, validated_data):
            username = validated_data['f_name'] + validated_data['l_name']
            password = validated_data['f_name'] + validated_data['l_name'] +"1234"
            user = User.objects.create_client(username, validated_data['f_name'],validated_data['l_name'], validated_data['p_email'],password)
            user.set_password(password)
            user.save()
            member = Member.objects.create(validated_data)
            return member

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =  (
            "id",
            "name"
        )