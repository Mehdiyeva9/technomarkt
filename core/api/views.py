from rest_framework import views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import (
    Bannerimage, Category, Brand, Payment, Product, FavoriteList, Basket, 
    CareerForm, HelpForm, Question, SocialMedia, SiteSettings
)
from core.api.serializers import (
    UserCreateSerializer, BannerSerializer, CategorySerializer, BrandSerializer, PaymentSerializer, ProductSerializer, 
    ProductRetrieveSerializer, FavoriteListSerializer, FavoriteListCreateSerializer,BasketSerializer, BasketCreateSerializer,
    CareerFormSerializer,HelpFormSerializer, QuestionSerializer, SocialMediaSerializer, SiteSettingsSerializer
)

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class BannerImageListAPIView(ListAPIView):
    queryset = Bannerimage.objects.all()
    serializer_class = BannerSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BestSellingProductListAPIView(ListAPIView):
    def get_queryset(self):
        return Product.objects.order_by("-number_of_sales")[:12]
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer
    lookup_field = "id"

class DiscountedProductListAPIView(ListAPIView):
    def get_queryset(self):
        return Product.objects.filter(discount_status = True)[:12]
    serializer_class = ProductSerializer

class CategoryProductListAPIView(ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs.get("id")
        category = Category.objects.get(id = category_id)
        return Product.objects.filter(
            category = category
        )
    serializer_class = ProductSerializer

class UserFavoriteListListAPİView(ListAPIView):
    def get_queryset(self):
        return FavoriteList.objects.filter(
            user = self.request.user
        )
    serializer_class = FavoriteListSerializer

class FavoriteListListAPIView(ListAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = (IsAdminUser, )

class FavoriteListCreateAPIView(CreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class BasketListAPIView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAdminUser, )

class UserBasketListAPIView(ListAPIView):
    def get_queryset(self):
        return Basket.objects.filter(
            user = self.request.user
        )
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated, )

class BasketCreateAPIView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CareerFormCreateAPIView(CreateAPIView):
    queryset = CareerForm.objects.all()
    serializer_class = CareerFormSerializer

class HelpFormCreateAPIView(CreateAPIView):
    queryset = HelpForm.objects.all()
    serializer_class = HelpFormSerializer

class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer