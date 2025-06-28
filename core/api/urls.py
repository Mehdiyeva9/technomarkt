from django.conf import urls
from core.api import views
from django.urls import path

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('bannerimage-list/', views.BannerImageListAPIView.as_view()),
    path('category-list/', views.CategoryListAPIView.as_view()),
    path('brand-list/', views.BrandListAPIView.as_view()),
    path('payment-list/', views.PaymentListAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('bestselling-list/', views.BestSellingProductListAPIView.as_view()),
    path('product-retrieve/<id>/', views.ProductRetrieveAPIView.as_view()),
    path('discount-list/', views.DiscountedProductListAPIView.as_view()),
    path('category-product-list/<id>/', views.CategoryProductListAPIView.as_view()),
    path('user-favorite-list/', views.UserFavoriteListListAPİView.as_view()),
    path('favorite-list/', views.FavoriteListListAPIView.as_view()),
    path('favorite-create/', views.FavoriteListCreateAPIView.as_view()),
    path('user-basket-list/', views.UserBasketListAPIView.as_view()),
    path('basket-list/', views.BasketListAPIView.as_view()),
    path('basket-create/', views.BasketCreateAPIView.as_view()),
    path("career-create/", views.CareerFormCreateAPIView.as_view()),
    path('help-create/', views.HelpFormCreateAPIView.as_view()),
    path('question-list/', views.QuestionListAPIView.as_view()),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view()),
    path('settings-list/', views.SiteSettingsListAPIView.as_view())
]