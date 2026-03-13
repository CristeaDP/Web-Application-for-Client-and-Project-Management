from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_shop/", views.add_shop, name="add_shop"),
    path("add_person/", views.add_person, name="add_person"),
    path("add_membership/", views.add_membership, name="add_membership"),
    path("display/", views.display_data, name="display_data"),
    path('delete_shop/<int:id>/', views.delete_shop, name='delete_shop'),
    path('delete_person/<int:id>/', views.delete_person, name='delete_person'),
    path('manage/', views.manage_database, name='manage_database'),
    path('delete_membership/<int:id>/', views.delete_membership, name='delete_membership'),
    path('modify-data/', views.modify_data, name='modify_data'),
    path('edit-shop/<int:id>/', views.edit_shop, name='edit_shop'),
    path('edit-person/<int:id>/', views.edit_person, name='edit_person'),
    path('edit-membership/<int:id>/', views.edit_membership, name='edit_membership'),
]
