from django.contrib import admin
from core.models import (
    Bannerimage, Category, Brand, Payment, Product, FavoriteList, Basket, ProductAbout,
    ProductComment, CareerForm, HelpForm, Question, SocialMedia, SiteSettings
)

admin.site.register(Bannerimage)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(FavoriteList)
admin.site.register(Basket)
admin.site.register(ProductAbout)
admin.site.register(ProductComment)
admin.site.register(CareerForm)
admin.site.register(HelpForm)
admin.site.register(Question)
admin.site.register(SocialMedia)
admin.site.register(SiteSettings)