
Authentication and Notification Service
============

This project provides an authentication service using JWT (JSON Web Token) and a notification service to send OTPs (One-Time Passwords) via abstractions like email, Telegram, and SMS. The project utilizes Django, Django REST Framework, Celery, and Docker Compose for easy deployment and scalability.notification service will validate user 
header Authorization request through a gRPC server with authentication server through port 50051.

Features
========
- User authentication using JWT
- OTP generation and sending via email, Telegram, and SMS
- Token validation using gRPC Inner Service Communications
- Docker Compose setup for easy deployment
- Comprehensive test suite for Authentication Service
- Swagger documentation available at `localhost:8000/user/swagger/` (port 8000) and `localhost:8001/notification/swagger/` (port 8001)

Architecture
============

High-Level Architecture
-----------------------

1. **Authentication Service**: Handles user authentication and token management using JWT.
2. **Notification Service**: Sends OTPs via email, Telegram, and SMS. Authenticates requests via gRPC.
3. **Database**: PostgreSQL database to store user data.
4. **Task Queue**: Celery for handling asynchronous tasks.
5. **Message Broker**: Redis for Celery message broker.


Detailed Architecture
---------------------

- **User**: Interacts with the system via API endpoints.
- **Django REST Framework**: Provides the API endpoints for authentication and OTP requests.
- **gRPC Client**: Used by the notification service to authenticate requests.
- **Celery Workers**: Execute asynchronous tasks for sending OTPs.
- **Redis**: Message broker for Celery.
- **PostgreSQL**: Database for storing user information.


Getting Started
===============

Prerequisites
-------------
- Docker
- Docker Compose

Installation
------------
1. Clone the repository::

    git clone https://github.com/meysamkheyrollah/SimpleMicroService.git
    

2. Create Compose Network::

    docker network create backend


3. Build and run the services using Docker Compose in Each Service Directory::

    docker-compose up --build

4. Run Authentication service Tests::

    docker-compose exec auth python manage.py test


API Endpoints
=============

Authentication Service
----------------------

- **Login**: ``localhost:8000/user/login/`` (POST)

  Request::
  
    {
      "phone_number": "yourusername",
      "password": "yourpassword"
    }

  Response::
  
    {
      "access": "your-access-token",
      "refresh": "your-refresh-token"
    }

- **Token Refresh**: ``localhost:8000/user/refresh/`` (POST)

  Request::
  
    {
      "refresh": "your-refresh-token"
    }

  Response::
  
    {
      "access": "new-access-token"
    }

- **Sign Up**: ``localhost:8000/user/signup/`` (POST)

  Request::
  
    {
      "phone_number": "newusername",
      "national_id": "newpassword",
      "password": "newuser@example.com"
    }

  Response::
  
    {
      "phone_number": "newusername",
      "national_id": "newpassword",
      "password": "newuser@example.com"
    }

Notification Service
--------------------

- **Send OTP via Mobile**: ``localhost:8001/notification/mobile-otp/`` (POST)
You should only provide access token through headers with Authorization KEY
application will extract your phone number in a grpc manner but for simplicity only will
be checked with user_id but anything is possible 

  Response::
  
    {
      "message": "OTP has been sent to user"
    }

- **Send OTP via Telegram**: ``localhost:8001/notification/telegram-otp/`` (POST)



  Response::
  
    {
      "message": "Telegram code has been sent to user"
    }

- **Send OTP via Email**: ``localhost:8001/notification/email-otp/`` (POST)



  Response::
  
    {
      "message": "Email has been sent to user"
    }

Running Tests
=============
Run the tests using the following command::

    docker-compose exec auth python manage.py test

Swagger Documentation
=====================
Swagger documentation for the API endpoints is available at:

- Authentication Service: `http://localhost:8000/user/swagger/`
- Notification Service: `http://localhost:8001/notification/swagger/`


Notes
-----
- Ensure that the ``grpc_service`` directory contains your gRPC server code.
- Adjust the service names, build contexts, and commands as necessary to fit your project structure.

Conclusion
==========
This project provides a robust and scalable solution for user authentication and OTP notifications. By leveraging Docker Compose, the setup and deployment processes are simplified, allowing you to focus on developing and improving your application.

Feel free to contribute to the project or raise issues if you encounter any problems.



PLEASE IF YOU REJECTED LET ME KNOW WITH TECHNICAL FEEDBACK, Meysam Kheyrollan Nejad
