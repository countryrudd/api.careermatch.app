from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()

router.register(r'company_positions', views.CompanyPositionViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('github/repositories/', views.RepositoryView.as_view()),
]
