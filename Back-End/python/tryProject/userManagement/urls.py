from rest_framework import routers
from userManagement.api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/userManagement',LeadViewSet,'userManagementA')

urlpatterns =  router.urls
