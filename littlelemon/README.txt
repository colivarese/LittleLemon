URLS:

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

users:
    -admin/password@123
    -test/password@123

In both cases email is : ""