from django.conf.urls import url

from views import TweetDetailView, TweetListView, TweetCreateView

urlpatterns = [
    url(r'^list/', TweetListView.as_view(), name='list'),
    url(r'^detail/', TweetDetailView.as_view(), name='detail'),
    url(r'^create/', TweetCreateView.as_view(), name='create'),

]
