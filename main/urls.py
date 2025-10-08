from django.urls import path
from main.views import show_main, create_product, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_products, delete_products, add_product_ajax, register_ajax, login_ajax, edit_product_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_products, name='edit_product'),
    path('product/<uuid:id>/delete', delete_products, name='delete_product'),
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('product/<uuid:id>/edit-ajax/', edit_product_ajax, name='edit_product_ajax'),

]