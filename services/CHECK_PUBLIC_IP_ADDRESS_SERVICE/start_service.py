"""
Author : LA
Description : When your public IP has changed the new Public IP will be send via mail
Version : Public V1
"""


from .get_public_ip import get_public_ip
from .regex import check_ip
import time



class Check_IP():
    
    
    def __init__(self, logger=object, mail=object) -> None :
        """
        Description : Init log for this instance, init mail to get ready to connect to SMTP and IMAP
        Return : None
        """
        
        self.logger = logger
        self.logger.info("CPIAS - Logger Linked with service.")
        
        self.mail = mail # Send logger object to log mail data and return mail object
        self.logger.info("CPIAS - Mail Linked with service.")
        
        self.logger.info("CPIAS - Getting Public IP...")
        self.actual_ip = get_public_ip() # Start with actual Public IP
        
        self.ip = str

        self.logger.info("CPIAS - Verifying Public IP...")
        if not check_ip(ip=self.actual_ip) :
            
            self.logger.info("CPIAS - Error - Query didn't return IP. Quitting program...")
            exit()
            
        self.main()


    def main(self) -> None :
        """
        Description : Init timeout and get local time (EPOCH) call service as first function call and recall service function when timeout
        Return : None
        """
        
        self.logger.info("CPIAS - Starting service...")
        
        self.logger.info("CPIAS - Time setup...")
        seconds_to_wait = 60 * 30 # 1800 Secondes = 30 minutes
        timeout = time.time() + seconds_to_wait
        
        self.logger.info("CPIAS - Joining service...")
        self.service() # Do function call before while - Do While statement
        
        while 1 : # Keep program running. Note : Can also use bash to keep program running from shell script
            
            if time.time() > timeout :
                
                self.logger.info("CPIAS - Timeout - Rejoining service...")
                self.service()
                self.logger.info("CPIAS - Timeout - Left service.")
                timeout = time.time() + seconds_to_wait
            
               
    def service(self) -> None:
        """
        Description : Check Public IP address from external server, if Public IP has changed then send new IP to receiver else take a break and check again
        Return : None
        """
        self.logger.info("CPIAS - Fetching Public IP...")
        self.ip = get_public_ip() # Get Public IP

        self.logger.info("CPIAS - Verifiying Public IP...")
        if (check_ip(ip=self.ip) and self.actual_ip != self.ip): # Send Mail only if Public IP is different from actual Public IP
            
            self.logger.info("CPIAS - Public IP has been changed ! New Public IP is : {0}".format(self.ip))
            self.actual_ip = self.ip # Put new IP as actual IP because IP has been changed
            
            self.mail.connect_to_smtp() # Connect to SMTP server to send new IP to receiver
            
            self.mail.send_email(f'[ MESSAGE ] Hi ! This is your new public IP address : {self.actual_ip}. Thank you.') # Send Public IP to receiver
            
            self.mail.quit_smtp() # Terminate SMTP session
            
        else :
            self.logger.info("CPIAS -  Public IP not changed, actual Public IP is : {0}".format(self.actual_ip))
        
        self.logger.info("CPIAS - Task done. Quitting service...")
        