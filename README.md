# gas_utilit_APIs

# Gas Utility Service API Documentation

## Overview
The **Gas Utility Service API** is a Django-based web application designed to handle service requests, support tickets, and user management for a gas utility company. It includes authentication, CRUD operations, and a dashboard for administrators.

## Features
- **User Authentication** ( Login, Logout)
- **Service Requests Management** (Create, View, )
- **Support Ticket System** (Create, View, Track)
- **Admin Dashboard** (User statistics, request & ticket tracking)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3
- Django
- Django REST Framework (DRF)
- SQLite (for database management)

### Steps

1. **Create a Superuser** (For admin access)
   
   python manage.py createsuperuser

2. **Run the Server**

   python manage.py runserver

3. **Access the API**
   - Open `http://127.0.0.1:8000/api/`
   - Use API clients like Postman or cURL for testing

## API Endpoints

### Users
| Method | Endpoint                | Description          |
|--------|-------------------------|----------------------|
| POST   | `/api/user/login/`      | User login           |
| POST   | `/api/user/logout/`     | User logout          |
| GET    |'/api/users/dashboard/'  | All users Dashboard  |


### Service Requests
| Method | Endpoint                             | Description                 |
|--------|-----------------------------------|--------------------------- -|
| GET    | `api/service-requests/ticket_list`| List all requests           |
| POST   | `api/service-requests/create/`    | Create a service request    |
| GET    | `/api/service-requests/<id>/`     | Retrieve a specific request |


### Support Tickets
| Method | Endpoint                            | Description             |
|--------|-------------------------------------|-----------------------  |
| GET    | `api/support/ticket_list_api`       | List all tickets        |
| GET   | `/api/support/create/`               | Create a support ticket |
| GET    | `/api/tickets/<id>/`                | Retrieve a ticket       |
| PUT    | `/api/tickets/<id>/update-status/ ` | Update status a ticket  |
| DELETE | `/api/support/<id>/`                | Get with id a ticket    |

