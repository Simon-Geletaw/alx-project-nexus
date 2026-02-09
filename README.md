# E-Commerce API

Professional, production-ready Django REST API for a basic e-commerce backend. It provides secure account management, JWT authentication, and CRUD operations for categories and products.

## Table of contents
1. Overview
2. Key features
3. Tech stack
4. Project structure
5. Getting started
6. Configuration
7. Swagger / OpenAPI output
8. Authentication
9. Endpoint reference
10. Status codes
11. Contact

## Overview
This service exposes REST endpoints for user accounts, categories, and products. It is designed to be a clean backend foundation that can be consumed by web or mobile clients.

## Key features
- JWT-based authentication and authorization
- User registration, profile retrieval, and password change
- Category CRUD operations
- Product CRUD operations with category association
- Django admin access for management

## Tech stack
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL support via psycopg2-binary
- drf-spectacular for OpenAPI

## Project structure
- E_Commerce/ - Django project settings and URLs
- apps/ - Application modules
  - accounts/ - User management and authentication
  - categories/ - Category domain logic
  - products/ - Product domain logic
- swagger/ - OpenAPI specification

## Getting started

### Prerequisites
- Python 3.x
- A PostgreSQL database (recommended for production)

### Installation
1. Create and activate a virtual environment.
2. Install dependencies from requirements.txt.
3. Run migrations.
4. Start the server.

### Example workflow
1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Configuration
Common environment variables used for deployment and security:
- DEBUG: Enable or disable debug mode
- ALLOWED_HOSTS: Comma-separated hosts allowed by Django
- CSRF_TRUSTED_ORIGINS: Allowed CSRF origins
- DATABASE_URL: Database connection string

## Swagger / OpenAPI output
The OpenAPI 3.0.3 specification is available at:
- [swagger/swagger.yml](swagger/swagger.yml)

**API metadata from the spec**
- Title: E-Commerce
- Version: 1.0
- Description: E-Commerce API that handles user accounts, products, categories
- Default server: http://127.0.0.1:8000
- Security: HTTP Bearer JWT (BearerAuth)

## Authentication
Most endpoints are protected by JWT.
- Obtain a token via POST /api/.
- Include the token in the Authorization header as: Bearer <token>.

## Endpoint reference

### Admin
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| GET | /admin/ | Django admin access | Session | None |

### Authentication (Token)
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| POST | /api/ | Issue or refresh JWT token | None | email, password |

### Accounts
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| GET | /accounts/Me/ | Retrieve authenticated user details | Bearer | None |
| POST | /accounts/register/ | Register a new user | None | email, password, is_staff, is_active, first_name, last_name, phone_number |
| POST | /accounts/change-password/ | Change password for the authenticated user | Bearer | old_password, new_password, confirm_new_password |

### Categories
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| GET | /categories/ | List all categories | Bearer | None |
| POST | /categories/create/ | Create a category | Bearer | name |
| GET | /categories/{id}/ | Retrieve a category by ID | Bearer | None |
| PUT | /categories/{id}/update/ | Update a category by ID | Bearer | name |
| DELETE | /categories/{id}/delete/ | Delete a category by ID | Bearer | None |

### Products
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| GET | /products/ | List all products | Bearer | None |
| POST | /products/create/ | Create a product | Bearer | name, description, price, category_id |
| GET | /products/{id}/ | Retrieve a product by ID | Bearer | None |
| PUT | /products/{id}/update/ | Update a product by ID | Bearer | name, description, price, category_id |
| DELETE | /products/{id}/delete/ | Delete a product by ID | Bearer | None |

### Additional endpoint in spec
| Method | Path | Purpose | Auth | Request body |
| --- | --- | --- | --- | --- |
| GET | /accounts/user | Retrieve a list of products (as defined in the spec) | Bearer | None |

## Status codes
Common responses used across endpoints:
- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

## Contact
Maintainer: Simon Geletaw
Email: simongeletaw2@gmail.com
