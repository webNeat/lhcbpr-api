from django.conf.urls import url, include
from rest_framework import routers
from lhcbpr_api import views

router = routers.DefaultRouter()

router.register(r'applications', views.ApplicationViewSet)
router.register(r'versions', views.ApplicationVersionViewSet)
router.register(r'options', views.OptionViewSet)
router.register(r'attributes', views.AttributeViewSet)
router.register(r'setups', views.SetupProjectViewSet)
router.register(r'descriptions', views.JobDescriptionViewSet)
router.register(r'thresholds', views.AttributeThresholdViewSet)
router.register(r'handlers', views.HandlerViewSet)
router.register(r'jobs', views.JobViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'lhcbpr_api.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )
