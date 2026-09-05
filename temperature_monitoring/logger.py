import logging
import os
from datetime import datetime

class TemperatureLogger:
    def __init__(self, log_file='temperature_errors.log'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logs_dir = os.path.join(current_dir, "logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        self.log_path = os.path.join(logs_dir, log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        self.log_path = os.path.join(logs_dir, log_file)
        
        self.logger = logging.getLogger('TemperatureSensor')
        self.logger.setLevel(logging.DEBUG)
        
        #file handler
        file_handler = logging.FileHandler(self.log_path)
        file_handler.setLevel(logging.ERROR)
        
        #format
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        #add handler
        self.logger.addHandler(file_handler)
        
    def log_error(self, error_message):
        self.logger.error(error_message)
    
    def log_info(self, info_message):
        self.logger.info(info_message)
    