import logging

# logging.INFO profile to redirect to app.log
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)