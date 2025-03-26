"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/service-requests/', include('service_requests.urls')),
    path('api/support/', include('support.urls')),

]




# ├── gas_utility
# │   ├── settings.py
# │   ├── urls.py
# │   ├── wsgi.py
# │   ├── asgi.py
# │   ├── __init__.py
# │
# ├── users
# │   ├── models.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── forms.py
# │   ├── admin.py
# │   ├── templates
# │   │   ├── users
# │   │   │   ├── register.html  # Improved UI with Bootstrap
# │   │   │   ├── login.html  # Enhanced user experience
# │   │   │   ├── dashboard.html  # Dashboard with navigation and user details
# │
# ├── service_requests
# │   ├── models.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── forms.py
# │   ├── admin.py
# │   ├── templates
# │   │   ├── service_requests
# │   │   │   ├── create_request.html  # Simple and clean form design
# │   │   │   ├── request_list.html  # User-friendly request tracking page
# │   │   │   ├── request_detail.html  # Improved request details page with status updates
# │
# ├── support
# │   ├── models.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── templates
# │   │   ├── support
# │   │   │   ├── chat.html  # Interactive chat interface
# │
# ├── static
# │   ├── css
# │   │   ├── styles.css  # Improved styling for better UX
# │   ├── js
# │   │   ├── main.js  # Added interactivity with JavaScript
# │
# ├── templates
# │   ├── base.html  # Modern UI with a responsive navbar
# │
# ├── db.sqlite3
# ├── manage.py
