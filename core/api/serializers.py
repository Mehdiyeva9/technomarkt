from rest_framework import serializers
from core.models import (
    Bannerimage, Category, Brand, Payment, Product, FavoriteList, Basket, ProductAbout,
    ProductComment, CareerForm, HelpForm, Question, SocialMedia, SiteSettings
)
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        validate_password(attrs["password"])
        return attrs
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username= username,
            password= password
        )
        return user
    
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bannerimage
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class ProductAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAbout
        fields = "__all__"

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = "__all__"

class ProductRetrieveSerializer(serializers.ModelSerializer):
    comment = ProductCommentSerializer()
    about = ProductAboutSerializer()
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("image", "name", "price", "raiting")

class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = "__all__"

class FavoriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ("product", )

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"

class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("product", )

class CareerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = "__all__"

class HelpFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpForm
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"