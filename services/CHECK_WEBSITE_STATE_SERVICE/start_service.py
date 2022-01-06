"""
Author : LA
Description : When your website is down an alert will be send via mail
Version : Public V1
"""


from .get_website_status import get_website_status
import time


class Check_Website_Status():
    
    def __init__(self, logger=object, mail=object) -> None :
        """
        Description : Init log for this instance, init mail to get ready to connect to SMTP and IMAP
        Return : None
        """
        self.logger = logger
        self.logger.info("CWSS - Logger Linked with service.")
        
        self.mail = mail # Send logger object to log mail data and return mail object
        self.logger.info("CWSS - Mail Linked with service.")
        
        self.main()


    def main(self) -> None :
        """
        Description : Init timeout and get local time (EPOCH) call service as first function call and recall service function when timeout
        Return : None
        """
        
        self.logger.info("CWSS - Starting Service...")
        
        self.logger.info("CWSS - Time setup...")
        
        seconds_to_wait = 60 * 30 # 1800 Secondes = 30 minutes
        timeout = time.time() + seconds_to_wait
        
        self.logger.info("CWSS - Joining service...")
        self.service() # Do function call before while - Do While statement style
        
        while 1 : # Keep program running. Note : Can also use bash to keep program running from shell script
            
            if time.time() > timeout :
                
                self.logger.info("CWSS - Timeout - Rejoining service...")
                self.service()
                self.logger.info("CWSS - Timeout - Left service.")
                timeout = time.time() + seconds_to_wait

            
    def service(self) -> None:
        """
        Description : Check Website status, if Website is down with a 404 error then send alert via mail else take a break and check again
        Return : None
        """
        self.logger.info("CWSS - Getting Website status...")
        status = get_website_status() # Get Website Status

        self.logger.info("CWSS - Verifiying Website status...")
        
        if not status: # Send Mail only if Public IP is different from actual Public IP
            
            self.logger.info("CWSS - Website is unreachable.")
            
            self.mail.connect_to_smtp() # Connect to SMTP server to send new IP to receiver
            
            self.mail.send_email(msg_content="[ MESSAGE ] Hi ! Vortex Website is unreachable. Thank you.") # Send Public IP to receiver
            
            self.mail.quit_smtp() # Terminate SMTP session
            
        else :
            self.logger.info("CWSS - Website is reachable.")
            
        self.logger.info("CWSS - Task done. Quitting service...")