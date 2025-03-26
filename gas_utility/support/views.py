from django.shortcuts import render, redirect, get_object_or_404
from .models import SupportTicket
from .forms import SupportTicketForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import SupportTicketSerializer

#  API: Create Ticket
class CreateTicketAPI(generics.CreateAPIView):
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#  API: List User's Tickets
class ListTicketsAPI(generics.ListAPIView):
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SupportTicket.objects.filter(user=self.request.user)

#  API: Get Ticket Detail
class TicketDetailAPI(generics.RetrieveAPIView):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

# API: Update Ticket Status
@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def update_ticket_status(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk)
    
    if ticket.user != request.user:
        return Response({"error": "You can only update your own tickets."}, status=403)

    status = request.data.get("status")
    if status not in ['open', 'in_progress', 'resolved']:
        return Response({"error": "Invalid status value."}, status=400)

    ticket.status = status
    ticket.save()
    
    return Response({"message": "Status updated successfully."}, status=200)





