from django.db import models
from django.contrib.auth.models import User

class Bannerimage(models.Model):
    image = models.ImageField(upload_to="pro_img/")

    def __str__(self):
        return "Banner image"

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="pro_img/", blank=True, null=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=15)
    logo = models.ImageField(upload_to="pro_img/", blank=True, null=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    icon = models.ImageField(upload_to="pro_img/")
    link = models.URLField(max_length=256)

    def __str__(self):
        return self.link

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="pro_img/")
    price = models.IntegerField(default=100)
    discount_price = models.IntegerField(default=0)
    stock_number = models.CharField(max_length=15)
    content = models.TextField()
    raiting = models.FloatField(default=0)
    discount_status = models.BooleanField(default=False)
    number_of_likes = models.IntegerField(default=0)
    number_of_sales = models.IntegerField(default=0)

    def __str__(self):
            return self.name
    
class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favori_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favori_items')

    def __str__(self):
        return self.product
    
class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="basket_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_basket")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product

class ProductAbout(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="abouts")

    def __str__(self):
        return self.title

class ProductComment(models.Model):
    name = models.CharField(max_length=20)
    rait = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    content = models.TextField()
    media = models.FileField(upload_to="pro_img/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.name

class CareerForm(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=256)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    cv_link = models.URLField(max_length=256)

    def __str__(self):
        return self.name
    
class HelpForm(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=30)
    mail = models.EmailField(max_length=256)
    subject = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.subject

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
class SocialMedia(models.Model):
    icon = models.ImageField(upload_to="pro_img/")
    link = models.URLField(max_length=256)

    def __str__(self):
        return "Social Media"
    
class SiteSettings(models.Model):
    header_adv_title1 = models.CharField(max_length=50)
    header_adv_subtitle1 = models.CharField(max_length=50)
    header_adv_text1 = models.TextField()
    header_adv_image1 = models.ImageField(upload_to="pro_img/")
    header_adv_title2 = models.CharField(max_length=50)
    header_adv_subtitle2 = models.CharField(max_length=50)
    header_adv_text2 = models.TextField()
    header_adv_image2 = models.ImageField(upload_to="pro_img/")
    header_adv_title3 = models.CharField(max_length=50)
    header_adv_subtitle3 = models.CharField(max_length=50)
    header_adv_text3 = models.TextField()
    header_adv_image3 = models.ImageField(upload_to="pro_img/")
    middle_title1 = models.CharField(max_length=50)
    middle_icon1 = models.ImageField(upload_to="pro_img/")
    middle_title2 = models.CharField(max_length=50)
    middle_icon2 = models.ImageField(upload_to="pro_img/")
    middle_title3 = models.CharField(max_length=50)
    middle_icon3 = models.ImageField(upload_to="pro_img/")
    middle_title4 = models.CharField(max_length=50)
    middle_icon4 = models.ImageField(upload_to="pro_img/")
    middle_adv_title = models.CharField(max_length=50)
    middle_adv_subtitle = models.CharField(max_length=50)
    middle_adv_text = models.TextField()
    middle_adv_image = models.ImageField(upload_to="pro_img/")
    footer_adv_title1 = models.CharField(max_length=50)
    footer_adv_subtitle1 = models.CharField(max_length=50)
    footer_adv_text1 = models.TextField()
    footer_adv_image1 = models.ImageField(upload_to="pro_img/")
    mail_for_subscribe = models.EmailField(max_length=256)
    footer_adv_title2 = models.CharField(max_length=50)
    footer_adv_subtitle2 = models.CharField(max_length=50)
    footer_adv_text2 = models.TextField()
    footer_adv_image2 = models.ImageField(upload_to="pro_img/")
    about_image = models.ImageField(upload_to='pro_img/')
    about_title = models.CharField(max_length=70)
    working_hours = models.TextField()
    location = models.TextField()

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Settings"

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            pass
        return super(SiteSettings, self).save(*args, **kwargs)