
from .viewsets.contact import ContactViewset
from .viewsets.ledger import NewLedgerTimeViewset
from .viewsets.profile import ProfileList, CreateMemberViewset,  ProfileRegViewSet, MembersViewset
from .viewsets.matter import MatterList, TaskViewset, TasksViewset, NewMatterViewset, NewTaskViewset
from .viewsets.category import CategoryViewset, SubCategoryViewset, ClassificationViewset


from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', ProfileList, 'profile')
router.register('profile-reg', ProfileRegViewSet, 'profile-reg')
router.register('matter', MatterList, "matter")
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

urlpatterns = router.urls
