import logging, sys

log = logging.getLogger(__name__)

class CriticalAppError(Exception):
    log.critical(Exception)

class InputValidationFailed(Exception):
    log.error(Exception)