from loguru import logger

id = "ingesta01"

logger.info(id + " - " + "Server started successfully.") # operaciones que funcionan correctamente
logger.warning(id + " - " + "Invalid configuration detected.") # No es un error
logger.error(id + " - " + "Failed to connect to the database.") # Errores comunes
logger.critical(id + " - " + "Unexpected system error occurred. Shutting down.") # Error crítico: crasheó
logger.success(id + " - " + "Data processing completed successfully.")
