from nautobot.api.routers import NetBoxRouter

from nautobot_topology_views.api import views

router = NetBoxRouter()

router.register("save-coords", views.SaveCoordsViewSet)
router.register("images", views.SaveRoleImageViewSet)
router.register("xml-export", views.ExportTopoToXML)

urlpatterns = router.urls
