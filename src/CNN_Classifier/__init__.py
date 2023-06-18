# Its custom type can be used in other projects as well

import os
import sys
import logging # python pre-built logging


#Message string:  ascii time, log level name, module (file you are running), message
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s ]"

# Create log directory
log_dir ="logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format= logging_str, # initialise logging stream

    handlers=[
        logging.FileHandler(log_filepath), # read the log file
        logging.StreamHandler(sys.stdout) # print log in terminal as well
    ]
)

logger = logging.getLogger("CNN_Classifier_Logger")