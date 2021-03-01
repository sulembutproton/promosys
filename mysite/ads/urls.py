# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
"""
from django.urls import path, reverse_lazy
from . import views

app_name='ads'

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('ads', views.ArticleListView.as_view(), name='all'),
    path('ads/<int:pk>', views.ArticleDetailView.as_view(), name='ads_detail'),
    path('ads/create',
        views.ArticleCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_create'),
    path('ads/<int:pk>/update',
        views.ArticleUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_update'),
    path('ads/<int:pk>/delete',
        views.ArticleDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ads_delete'),
]
"""


from django.urls import path, reverse_lazy
from . import views

app_name='ads'

urlpatterns = [
    path('', views.AdsListView.as_view()),
    path('ads', views.AdsListView.as_view(), name='all'),
    path('ads/<int:pk>', views.AdsDetailView.as_view(), name='ads_detail'),
    path('ads/create',
        views.AdsCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_create'),
    path('ads/<int:pk>/update',
        views.AdsUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ads_update'),
    path('ads/<int:pk>/delete',
        views.AdsDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ads_delete'),
]

