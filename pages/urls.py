from django.urls import path

from pages.views import home_page_view, create_email_view, create_order_view

app_name = 'pages'

urlpatterns = [
    path('email/', create_email_view, name='create_email'),
    path('order/', create_order_view, name='create-order'),
    path('', home_page_view),
]
