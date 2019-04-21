
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from healthkraft import views as core_views
from users import views as user_views
from bmi.views import  form_print, form_get


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='homenew.html'), name='home'),
    path('atkins/', core_views.atkins, name='atkins'),
    path('ketogenic/', core_views.ketogenic, name='ketogenic'),
    path('vegan/', core_views.vegan, name='vegan'),
    path('vegetarian/', core_views.vegetarian, name='vegetarian'),
    path('raw/', core_views.raw, name='raw'),
    path('zone/', core_views.zone, name='zone'),
    path('salads/', core_views.salads, name='salads'),
    path('soups/', core_views.soups, name='soups'),
    path('smoothies/', core_views.smoothies, name='smoothies'),
    path('food/', core_views.food, name='food'),
    path('proteins1/', core_views.proteins1, name='proteins1'),
    path('carb/', core_views.carb, name='carb'),
    path('fats/', core_views.fats, name='fats'),
    path('micronutrients/', core_views.micronutrients, name='micronutrients'),
    path('energy/', core_views.energy, name='energy'),
    path('aboutus/', core_views.aboutus, name='aboutus'),  
    path('fitness/', core_views.fitness, name='fitness'),  
    path('form_print/',form_print, name='form_print'),
    path('form_get/',form_get, name='form_get'),
]
'''path('signup/', core_views.signup, name='signup'),
path('signup/', core_views.signup, name='signup'),'''