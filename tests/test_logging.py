import os
import logging
from fastapi.testclient import TestClient
from app.main import app


def test_logging(caplog):
    # Activate the logging capture
    caplog.set_level(logging.INFO)

    # Configure logger to write to test.log in the logs folder
    log_filename = os.path.join("logs", "test.log")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a test client
    client = TestClient(app)

    # Make a POST request to trigger logging
    payload = {
        "name": "Test",
        "description": "Here is just to check if everything is okay ...",
    }
    with client as client:
        client.post("/items/", json=payload)

    # Check if the log message was captured
    assert any("Creating a new item" in record.message for record in caplog.records)
