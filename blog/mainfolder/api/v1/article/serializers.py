from rest_framework import serializers
from catalog.models import Article, User


class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(max_length=200)
    article_additional_title = serializers.CharField(max_length=400)
    article_text = serializers.CharField()

    def create(self, validated_data):
        validated_data.get('')
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("article_title", instance.title)
        instance.additional_title = validated_data.get("article_additional_title", instance.additional_title)
        instance.text = validated_data.get("article_text", instance.text)
        instance.save()
        return instance


class ArticleCreateSerializer(serializers.ModelSerializer):
    article_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    slug = serializers.SlugField(read_only=True, source='save')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='get_author_username')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
