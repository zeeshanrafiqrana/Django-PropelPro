import logging
from django.shortcuts import render

logger = logging.getLogger("apps.users.views")


# Create your views here.
def sentry_debug_view(request):
    logger.info("This is an informational message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
