import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Unable to connect to server")

print("Logging completed")