from django.urls import path
from .views import CreateTicketAPI, ListTicketsAPI, TicketDetailAPI, update_ticket_status

urlpatterns = [
    path('create/', CreateTicketAPI.as_view(), name='create_ticket_api'),
    path('ticket_list_api', ListTicketsAPI.as_view(), name='ticket_list_api'),
    path('<int:pk>/', TicketDetailAPI.as_view(), name='ticket_detail_api'),
    path('<int:pk>/update-status/', update_ticket_status, name='update_ticket_status_api'),
]

