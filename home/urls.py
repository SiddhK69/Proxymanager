from django.urls import path, re_path

from home import views
from home.views import Add_Data_PRX, Add_TimeTable, Edit_Data_PRX, Edit_TimeTable, add_stats, Edit_stats



urlpatterns = [ 
#Login
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),

#Proxy
    path('add_prx', Add_Data_PRX.as_view(), name="add_prx"),
    path('edit_prx/<str:pk>', Edit_Data_PRX.as_view(), name="edit_prx"),
    path('delete_prx/<str:pk>', views.delete_prx, name="delete_prx"),
    path('confirm_prx/<int:id>/<str:pk>', views.Confirm_PRX, name="Confirm_PRX"),
    path('userconfirm_prx/<int:idx>/show_prx/<int:id>/<str:pk>', views.get_proxys, name='show_prx'),
    path('Place_PRX/<str:pk>/<int:id>', views.Place_PRX, name="Place_PRX"),
    path('show_prx/<int:id>/<str:pk>', views.get_proxys, name="show_prx"),
    path('show_prx_all', views.All_Proxy, name='show_prx_NA'),
    path('delete-proxy', views.delete_prx_all, name='delete_prx_all'),
    path('locate_image/', views.locate_image, name='locate_image'),
    

#TimeTable
    path('add_tt', Add_TimeTable.as_view(), name="add_tt"),
    path('edit_tt/<str:id>', Edit_TimeTable.as_view(), name="edit_tt"),
    path('delete_tt/<str:id>', views.delete_tt, name="delete_tt"),
    path('show_tt/<str:id>', views.get_subs, name="show_tt"),

#Statistics
    path('add_stats', add_stats.as_view(), name="add_stats"),
    path('edit_stats/<str:pk>', Edit_stats.as_view(), name="edit_stats"),
    path('delete_stats/<str:pk>', views.delete_stats, name="delete_stats"),
    path('reset-stats', views.reset_stats, name="reset_stats"),
    path('download_data', views.download_data, name="download_data"),

#NonAdmin Paths
    path('user/', views.index_NA, name='home_NA'),
    re_path('show_prx_NA', views.All_Proxy, name='show_prx_NA'),

]