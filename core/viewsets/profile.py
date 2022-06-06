# Create your views here.
from ..models.profile import Profile, Member
from rest_framework import  viewsets, permissions
from django.shortcuts import get_object_or_404
from ..serializers.profile import ProfileSerializer, CreateMemberSerializer, MembersSerializer,  ProfileShortSerializer
from rest_framework.response import Response
        
class ProfileRegViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProfileShortSerializer

    def get_queryset(self):
        return self.request.user.profile.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileList(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.get(username=pk)
        profile = get_object_or_404(queryset, pk=1)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
class CreateMemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CreateMemberSerializer

class MembersViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MembersSerializer
