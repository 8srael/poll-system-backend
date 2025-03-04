from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login pour obtenir le token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Rafraîchir le token
]
