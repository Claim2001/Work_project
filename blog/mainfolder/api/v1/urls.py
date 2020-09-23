from django.urls import path

from api.v1.article.views import ArticleListSerik, ArticleCreateSerik, ArticleDeleteSerik, UserCreateSerik, \
    UserListViewSerik
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('articles/list/', ArticleListSerik.as_view()),
    path('articles/create/', ArticleCreateSerik.as_view()),
    path('articles/<int:pk>', ArticleDeleteSerik.as_view()),
    path('articles/register/', UserCreateSerik.as_view()),
    path('articles/user/list', UserListViewSerik.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
