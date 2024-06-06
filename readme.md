# Structured FastAPI PostgreSQL Docker

This is a simple example project demonstrating how to build a FastAPI application that interacts with a PostgreSQL database using Docker.

## Requirements

- Python 3.7+
- Docker

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eaedk/structured-fastapi-postgresql-docker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd structured-fastapi-postgresql-docker
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the PostgreSQL database using Docker Compose:

   ```bash
   docker-compose up -d
   ```

2. Run the FastAPI application:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the FastAPI Swagger documentation:

   Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs).

4. Test the endpoints using cURL or any HTTP client.

## Endpoints and cURL Commands

### Create a new item

```bash
curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"name": "Test Item", "description": "This is a test item"}'
```

### Retrieve an item by ID

```bash
curl -X GET "http://localhost:8000/items/{item_id}"
```

### Update an existing item

```bash
curl -X PUT "http://localhost:8000/items/{item_id}" -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "This item has been updated"}'
```

### Delete an item by ID

```bash
curl -X DELETE "http://localhost:8000/items/{item_id}"
```

Replace `{item_id}` with the actual ID of the item you want to interact with.

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Project Structure

```
structured-fastapi-postgresql-docker/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging_config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── models.py
│   │   ├── session.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── items.py
│   ├── Logs/
│   │   ├── .gitkeep
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── items.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_items.py
│   ├── test_logging.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

This README provides a comprehensive guide on how to set up, run, and test the application, along with details about the project structure and license.
```
