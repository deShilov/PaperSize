from django.urls import path
from .views import PaperList, PaperDetail, PaperCreate, PaperUpdate, PaperDelete, LoginView, RegisterView, Home
from django.contrib.auth.views import LogoutView


urlpatterns = [
	path('', Home.as_view(), name='home'),

	path('papers', PaperList.as_view(), name='papers'),

	path('paper/<int:pk>/', PaperDetail.as_view(), name='paper'),
	path('paper-create/', PaperCreate.as_view(), name='paper-create'),
	path('paper-update/<int:pk>', PaperUpdate.as_view(), name='paper-update'),
	path('paper-delete/<int:pk>', PaperDelete.as_view(), name='paper-delete'),

	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
	path('reg/', RegisterView.as_view(), name='register'),
]