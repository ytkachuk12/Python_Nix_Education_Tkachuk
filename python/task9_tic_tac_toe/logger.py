"""2 loggers. One for matches history, another for history between same players."""
import logging


# Create a custom logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

# Create handlers
match_file_handler = logging.FileHandler('matches.log')
revvanche_file_handler = logging.FileHandler('revanche.log')
match_file_handler.setLevel(logging.DEBUG)
revvanche_file_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
match_format = logging.Formatter('%(asctime)s - %(message)s')
revvanche_format = logging.Formatter('%(asctime)s - %(message)s')
match_file_handler.setFormatter(match_format)
revvanche_file_handler.setFormatter(revvanche_format)

# Add handlers to the logger
logger.addHandler(match_file_handler)
logger.addHandler(revvanche_file_handler)
