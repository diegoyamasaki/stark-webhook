import logging
import sys

import google.cloud.logging

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
client = google.cloud.logging.Client()
client.setup_logging()