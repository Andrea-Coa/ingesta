from loguru import logger

id = "ingesta05"

logger.info(id + " - " + "Server started successfully.")
logger.warning(id + " - " + "Invalid configuration detected.")
logger.error(id + " - " + "Failed to connect to the database.")
logger.critical(id + " - " + "Unexpected system error occurred. Shutting down.")
logger.success(id + " - " + "Data processing completed successfully.")
