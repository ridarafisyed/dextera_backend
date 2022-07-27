
from  django.urls import path

from .viewsets.address import StateViewset,CountyViewset,CityViewset,ZipCodeViewset,SelectCountyViewset
from .viewsets.contact import ContactViewset
from .viewsets.ledger import NewLedgerTimeViewset
from .viewsets.profile import ProfileList, CreateMemberViewset,  ProfileRegViewSet, MembersViewset, GetProfileViewSet, UpdateProfileViewSet
from .viewsets.firm import GetFirmAccountViewset, GetPaymentInfoViewset,GetBillingAddressViewset,PaymentInfoViewset,BillingAddressViewset, UploadFirmLogoViewset
from .viewsets.matter import MatterList, TaskViewset, TasksViewset, NewMatterViewset, NewTaskViewset
from .viewsets.category import CategoryViewset, SubCategoryViewset, ClassificationViewset
from .viewsets.member import ListMembersView, UpdateMemberView
from .viewsets.firm import FirmAccountViewset, GetFirmDetailViewSet, GetFirmSummaryViewSet

from rest_framework import routers

router = routers.DefaultRouter()

# register user 
router.register('profile', ProfileList, 'profile')
router.register('update-profile', UpdateProfileViewSet, 'update-profile')
router.register('get-profile', GetProfileViewSet, 'get-profile')

# register firm 
router.register('get-firm', GetFirmAccountViewset, 'get-profile')
router.register('create-firm', FirmAccountViewset, 'create-firm')
router.register('get-payment-info-reg', GetPaymentInfoViewset, 'get-payment-info')
router.register('get-bill-add-reg', GetBillingAddressViewset, 'get-bill-add')
router.register('payment-info-reg', PaymentInfoViewset, 'payment-info-reg')
router.register('bill-add-reg', BillingAddressViewset, 'bill-add-reg')
router.register('upload-logo', UploadFirmLogoViewset, 'upload-logo')

router.register('profile-reg', ProfileRegViewSet, 'profile-reg')
router.register('firm-detail', GetFirmDetailViewSet, 'firm-detail')
router.register('firm-summary', GetFirmSummaryViewSet, 'firm-summary')
router.register('matter', MatterList, "matter")
router.register('state', StateViewset, "state")
router.register('county', CountyViewset, "sounty")
router.register('city', CityViewset, "city")
router.register('zip-code', ZipCodeViewset, "zip-code")
router.register('select_county', SelectCountyViewset, "select-county")
router.register('new-matter', NewMatterViewset, "new-matter")

router.register('category', CategoryViewset, "category")
router.register('sub-category', SubCategoryViewset, "sub-category")
router.register('classification', ClassificationViewset, "classification")

router.register('tasks', TasksViewset, "tasks" )
router.register('task', TaskViewset, "task")
router.register('new-task', NewTaskViewset, "task")

router.register('add-time',NewLedgerTimeViewset, 'add-time')
router.register('members', MembersViewset, "members")
router.register('create-member', CreateMemberViewset, "create-member")

router.register('contact', ContactViewset, "contact")
# router.register('members-lists', ListMembersView.as_view(), "member-list")

urlpatterns = router.urls + [
    path('members-list/', ListMembersView.as_view()),
    path('member-update/<int:pk>/', UpdateMemberView.as_view()),
    # path('upload-logo/', UploadFirmLogoViewset.as_view()),
    # path('create-firm/', CreateFirmAccountViewSet.as_view())
]