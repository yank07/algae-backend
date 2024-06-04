# Algae Monitor Project

This project is a web application for monitoring algae in bodies of water. It allows citizen scientists and biologists to collaborate by tracking algae observations and requests for new observations.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Database Migration](#database-migration)
  - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Role-based access control (Biologists and Citizens)
- Create, read, update, and delete observations
- Request new observations
- View all requests (Biologists) or user-specific requests (Citizens)
- Swagger documentation for API endpoints

## Technology Stack

- Django
- Django REST Framework
- Django Simple JWT
- PostgreSQL
- React (Frontend)
- Tailwind CSS
- Axios

## Setup Instructions

### Prerequisites

- Python 3.x
- pip
- PostgreSQL
- Node.js and npm (for frontend)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/algae-monitor.git
   cd algae-monitor


### Create and activate a virtual environment

```sh
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
Install backend dependencies


pip install -r requirements.txt
Install frontend dependencies


cd frontend
npm install
cd ..
```

### Environment Variables
Create a .env file in the project root and add the following environment variables:

```sh
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=algae_monitor
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

```
### Database Migration
Create the database

```sh
createdb algae_monitor
### Apply migrations


python manage.py migrate
### Running the Server
Run the backend server

```sh
python manage.py runserver
Run the frontend development server
```


### API Endpoints
Swagger documentation is available at http://localhost:8000/swagger/.
