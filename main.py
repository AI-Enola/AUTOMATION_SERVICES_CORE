"""
Author : LA

Description : 
Allow to run multiple instance of services in one big instance. 
ASCore (Automation Services Core) init Mail object and Log object for services. Services is running into independant Thread.
This version does not support thread interaction.

Compatibility : Mac OS - GNU/Linux x86_x64 arm64
Version : V0.1 - Public Alpha

Sub Project : PUBLIC-IP-ADDRESS-ALERT-AUTOMATION V1 : https://github.com/AI-Enola/PUBLIC-IP-ADDRESS-ALERT-AUTOMATION

"""

# General Python Library
from _thread import *
from threading import Thread

# Project library
from log import *

from services.CHECK_PUBLIC_IP_ADDRESS_SERVICE.start_service import Check_IP
from services.CHECK_WEBSITE_STATE_SERVICE.start_service import Check_Website_Status

from email_io import MailIO


class ASCore():
    
    
    def __init__(self) -> None :
        """
        Description : Init log and mail - Log is using to log program stdout and Mail is to get SMTP ready for services. 
        Return : None
        """
        # Init logger with customizable parameters.
        self.logger = Log(log_in_file=True, encoding='utf-8', filename='log.txt', filemode='a', logger_name='AUTOMATION SERVICE CORE', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
        self.logger = self.logger.get_logger() # Get logger object to log stdout

        self.logger.info(f"MAIN : Logger Initialized.")
        
        # Init SMTP
        self.mail = MailIO(logger=self.logger)


    def main(self) -> None :
        """
        Description : Start services into independant thread
        Note : This is alpha version - Optimization and feature will be added later
        Return : None
        """
        
        self.logger.info(f"MAIN : Starting automation services...")

        ### I AGREE THIS CAN BE OPTIMIZED - VALIDATE TO BE UPDATE IN THE FUTURE
        
        # Init n Thread with service and args for them
        thread1 = Thread(target=Check_IP, args=(self.logger, self.mail))
        thread2 = Thread(target=Check_Website_Status, args=(self.logger, self.mail))
        
        # Main thread is not a deamon thread
        thread1.daemon = False
        thread2.daemon = False
        
        # Start n thread
        thread1.start()
        thread2.start()

        ### I AGREE THIS CAN BE OPTIMIZED - VALIDATE TO BE UPDATE IN THE FUTURE
             
# Start main program
if __name__ == "__main__":
    
    instance = ASCore() # Init program
    instance.main()