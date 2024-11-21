from .views import index
from django.urls import include, path
from . import views
from .views import SellerLoginView
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, SellerViewSet, ProductViewSet, CategoryViewSet, SubcategoryViewSet, CartViewSet, OrderViewSet, OrderItemViewSet, PurchaseOrderViewSet, PurchaseOrderItemViewSet, AddressViewSet


# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'purchaseorders', PurchaseOrderViewSet)
router.register(r'purchaseorderitems', PurchaseOrderItemViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_customer/', views.edit_customer, name='edit_customer'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('address/', views.address_list, name='address_list'),
    path('address/add/', views.address_create, name='address_create'),
    path('address/edit/<int:pk>/', views.address_edit, name='address_edit'),
    path('address/delete/<int:pk>/', views.address_delete, name='address_delete'),
    path("cart/", views.cart, name="cart"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('delete_item_in_cart/<int:id>/', views.delete_item_in_cart, name='delete_item_in_cart'),
    path('checkouts/', views.checkout, name='checkouts'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('product_list/',views.product_list,name='product_list'),
    path('search/', views.search_results, name='search_results'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('subcategory/<int:subcategory_id>/', views.subcategory_products, name='subcategory_products'),
    path('create_purchase_order/', views.CreatePurchaseOrderView.as_view(), name='create_purchase_order'),
    path('seller_purchase_orders/<int:purchase_order_id>/', views.purchase_order_details, name='purchase_order_details'),
    path('seller/purchase_orders/', views.seller_purchase_orders, name='seller_purchase_orders'),
    path('seller_login/', SellerLoginView.as_view(), name='seller_login'),
    path('reject_purchase_order/<int:purchase_order_id>/', views.reject_purchase_order, name='reject_purchase_order'),

    path('api/', include(router.urls)), 


]







