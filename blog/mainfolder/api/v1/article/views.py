from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.v1.article.serializers import ArticleCreateSerializer, UserSerializer, ArticleDeleteSerializer, \
    ArticleListSerializer
from catalog.models import Article


class ArticleCreateSerik(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = (AllowAny,)


class ArticleDeleteSerik(DestroyAPIView, RetrieveAPIView, UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDeleteSerializer
    lookup_url_kwarg = 'pk'
    permission_classes = (AllowAny,)


class ArticleListSerik(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        if self.request.GET.get('username', None):
            return Article.objects.filter(user__name=self.request.GET.get('username', None))
        return Article.objects.all()


class UserListViewSerik(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateSerik(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )