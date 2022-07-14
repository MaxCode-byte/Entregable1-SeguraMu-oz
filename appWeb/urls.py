
from unicodedata import name
from django.urls import path
from appWeb.views import *

urlpatterns = [
    #------------- Inicios ------------
    path('home', inicio, name= 'inicio'),
    path('djs/', Djs, name= 'djsinicio'),
    path('bartenders/', Bartenders, name= 'bartendersinicio'),
    path('mozos/', Mozos, name= 'mozosinicio'),
    path('suggestions/', Suggestions, name= 'suggestionsinicio'),
    #------------- Buscadores ------------
    path('djBusqueda/', djBusqueda, name='djBusqueda'),
    path('buscarDj/', djbuscar, name= 'djBuscar'),
    path('bartenderBusqueda/', bartenderBusqueda, name='bartenderBusqueda'),
    path('buscarBartender/', bartenderbuscar, name='bartenderBuscar'),
    path('mozoBusqueda/',mozoBusqueda, name='mozoBusqueda'),
    path('buscarMozo/',mozobuscar, name='mozoBuscar'),
       
    #--------------- Vista por clases ------------
    #------------------- Read ------------------
    path('Dj/list', djList.as_view(), name='dj_list'),
    path('Bartender/list', BartenderList.as_view(), name='Bartender_list'),
    path('Mozo/list', MozoList.as_view(), name='Mozo_list'),
    path('Suggestions/list', SuggestionsList.as_view(), name='Suggestion_list'),
    #------------------- Detail ------------------
    path('Dj/<pk>', djDetail.as_view(), name='Djdetail'),
    path('Bartender/<pk>', BartenderDetail.as_view(), name='Bartenderdetail'),
    path('Mozo/<pk>', MozoDetail.as_view(), name='Mozodetail'),
    path('Suggestions/<pk>', SuggestionsDetail.as_view(), name='Suggestionsdetail'),
    #------------------- Create ------------------
    path('Dj/new/', djCreate.as_view(), name='Djcreate'),
    path('Bartender/new/', BartenderCreate.as_view(), name='Bartendercreate'),
    path('Mozo/new/', MozoCreate.as_view(), name='Mozocreate'),
    path('Suggestions/new/', SuggestionsCreate.as_view(), name='Suggestionscreate'),
    #------------------- Update ------------------
    path('Dj/update/<pk>', djUpdate	.as_view(), name='Djupdate'),
    path('Bartender/update/<pk>', BartenderUpdate.as_view(), name='Bartenderupdate'),
    path('Mozo/update/<pk>', MozoUpdate.as_view(), name='Mozoupdate'),
    #------------------- Delete ------------------
    path('Dj/delete/<pk>', djDelete	.as_view(), name='Djdelete'),
    path('Bartender/delete/<pk>', BartenderDelete.as_view(), name='Bartenderdelete'),
    path('Mozo/delete/<pk>', MozoDelete.as_view(), name='Mozodelete'),
    path('Suggestions/delete/<pk>', SuggestionsDelete.as_view(), name='Suggestionsdelete'),
    #------------------- Login ------------------
    path('login', login_request, name='login'),
    #------------------- Reister ------------------
    path('register', register_request, name='register'),
    #------------------- LogOut ------------------
    path('logout', LogoutView.as_view(template_name='appWeb/logout.html'), name='logout'),
    #---------------------- Edit Profile ---------------------------
    path('editprofile', editProfile, name='editprofile'),
    #---------------------- About Us ---------------------------
    path('aboutus', AboutUs, name='aboutus'),
]
