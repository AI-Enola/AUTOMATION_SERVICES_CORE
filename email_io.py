"""
Author : LA
Description : Connect to SMTP server and send mail to receiver
Version : Public V1

"""

#import imaplib
import smtplib 
from email.message import EmailMessage

# More secure way to store login info in env : 
# EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# EMAIL_ADDRESS_DEST = os.environ.get('EMAIL_ADDRESS_DEST')

class MailIO():

    def __init__(self, logger=object) -> None:
        """
        Description : Call logger and init email source, email destination and email password
        EMAIL_ADDRESS and EMAIL_PASSWORD is the mail sender and the receiver will get mail from email of sender.
        Return : None
        """
        self.logger = logger
        
        # Sender
        self.EMAIL_ADDRESS = 'EMAIL_ADDRESS'
        self.EMAIL_PASSWORD = 'EMAIL_PASSWORD'
        
        # Receiver
        self.EMAIL_ADDRESS_DEST = 'DESTINATION EMAIL ADDRESS'
        
        # SMTP SERVER INFO
        self.SMTP = 'smtp-mail.outlook.com' # Example with outlook SMTP server domain - CAN BE CHANGED
        self.SMTP_PORT = 587 # Example with outlook SMTP server port - CAN BE CHANGED

    
    def connect_to_smtp(self) -> None:
        """
        Description : Connect to SMTP server using SMTP domain and server port
        Return : None
        """
        
        
        self.logger.info("MAIL - Init connection with server SMTP...")
        self.smtp_server = smtplib.SMTP(self.SMTP, self.SMTP_PORT)
        
        try:
            self.logger.info("MAIL - Init EHLO...")
            self.smtp_server.ehlo()
            
            self.logger.info("MAIL - Starting TLS...")
            self.smtp_server.starttls()
            self.smtp_server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            
        except:
            self.logger.info("MAIL - Error - Connection with server SMTP failed !")
            raise
        
        self.logger.info(" MAIL - Connection with server SMTP established.")
    
    

        
    def quit_smtp(self) -> None :
        """
        Description : Terminate SMTP session with SMTP server
        Return : None
        """
        self.logger.info("MAIL - Quitting SMTP server...")
        self.smtp_server.quit()
        self.logger.info("MAIL - Disconnected from SMTP server.")
    
    
    
    ## SUPPOSED TO BE DELETED IN PUBLIC VERSION BUT THERE IS FUNCTIONS TO USE IMAP AND QUIT IT
    
    
    # def connect_to_imap(self) -> None:
    #     OUTLOOK_IMAP = 'outlook.office365.com'
    #     OUTLOOK_IMAP_PORT = 993
        
    #     self.logger("Init connection with server IMAP...")
    #     self.imap_server = imaplib.IMAP4_SSL(OUTLOOK_IMAP, OUTLOOK_IMAP_PORT)
    #     self.imap_server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
        
        
    # def quit_imap(self) -> None :
    #     self.imap_server.close()
    #     self.imap_server.logout()
        
    # USE IMAP TO RECEIVE MESSAGE
    
    # def receive_email(self) -> None:
    #     self.imap_server.select('inbox')
    #     status, data = self.imap_server.search(None, '(FROM {} SUBJECT "BotWeb GIVE ME IP PUBLIC")'.format(self.EMAIL_ADDRESS_DEST))
        
    #     if not data[0]:
    #         print("[ WARNING ] No mail has been found, try again !")
    #         return None
    #     else :
    #         print("[ WARNING ] Mail has been found.")
            
    #         for num in data[0].split():
    #                 status, data = self.imap_server.fetch(num, '(RFC822)')
    #                 email_msg = data[0]
    #                 print(email_msg)
    #                 print(status)
    #                 break
                
    #         self.imap_server.store(num, "+FLAGS", "\\Deleted") # Delete mail
        
        
    # USE STMP TO SEND MESSAGE
    def send_email(self,msg_content=str) -> None:
        """
        Description : Get data as function parameter and wrap data into message and send it to receiver
        Return : None
        """
        
        self.logger.info("MAIL - Creating mail...")
        msg = EmailMessage()
        
        msg ['Subject'] = '[ RETURNED QUERY ] Message from BotWeb'
        msg ['From'] = self.EMAIL_ADDRESS
        msg ['To'] = self.EMAIL_ADDRESS_DEST

        msg.set_content(msg_content) # Message
        
        self.logger.info("Sending mail...")
        
        try:
            self.smtp_server.send_message(msg)
            
        except:
            self.logger.info("Error - Message not sended !")
            raise 
           
        self.logger.info("Mail sended.")