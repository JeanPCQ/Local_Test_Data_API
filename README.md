# Local Test Data API

A simple, fully containerized backend API for storing and retrieving JSON data locally using Docker and PostgreSQL.  
This project is designed for developers, analysts, or students who want a **ready-to-run backend environment** for testing, prototyping, or learning backend workflows.

---

## **Tech Stack**

- **FastAPI**: Python web framework for building the API  
- **SQLAlchemy**: ORM for interacting with PostgreSQL  
- **PostgreSQL**: Relational database for storing records  
- **Docker**: Containerization for reproducible environments  
- **Docker Compose**: Orchestrates the API and database services  

---

## **Features**

- Containerized API + database: **one command to start both services**  
- JSON storage: `POST /records` to save, `GET /records` to retrieve  
- Automatic database table creation  
- Retry logic for database connection: API waits until the database is ready  
- Data persistence using Docker volumes  

---

## **Getting Started**

### **Prerequisites**

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- Optional: [curl](https://curl.se/) or [Postman](https://www.postman.com/) for testing API

---

### **Run the project**

1. Clone the repository:

```bash
git clone https://github.com/JeanPCQ/Local_Test_Data_API.git
cd Local_Test_Data_API
