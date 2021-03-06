from django.conf.urls import url
from .views import (superuserpage, AddPlacementCreateView, AddPlacementListView, AddPlacementDeleteView,
                    AddPlacementDetailView, AddPlacementUpdateView, SubmissionsListView, SubmissionDetailView)

urlpatterns = [
    url(r'^$', superuserpage, name='superuserpage'),
    url(r'^create/$', AddPlacementCreateView.as_view(), name='addplacement'),
    url(r'^view/$', AddPlacementListView.as_view(), name='list'),
    url(r'^view/(?P<pk>[-\w]+)/$',
        AddPlacementDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', AddPlacementUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', AddPlacementDeleteView.as_view(), name='delete'),
    url(r'submission/$', SubmissionsListView.as_view(), name='sublist'),
    url(r'^submission/(?P<slug>[a-zA-Z0-9]*)/$',
        SubmissionDetailView.as_view(), name='subdetail'),
]
