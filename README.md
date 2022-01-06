# AUTOMATION_SERVICES_CORE

Compatibility : Mac OS & GNU/Linux (Using CURL CMD)

Version : V1 Public - Updated Late 2021

Description : Run different services on one Python instance. *More optimization and features need to be added in further version*

Sub Project : PUBLIC-IP-ADDRESS-ALERT-AUTOMATION

Link : https://github.com/AI-Enola/PUBLIC-IP-ADDRESS-ALERT-AUTOMATION

Note : 

Lines 28,29,32,3 and 36 in email_io.py need to be filled with your informations such as 

        # Sender
        self.EMAIL_ADDRESS = 'EMAIL_ADDRESS'
        self.EMAIL_PASSWORD = 'EMAIL_PASSWORD'
        
        # Receiver
        self.EMAIL_ADDRESS_DEST = 'DESTINATION EMAIL ADDRESS'
        
        # SMTP SERVER INFO
        self.SMTP = 'smtp-mail.outlook.com' # Example with outlook SMTP server domain - CAN BE CHANGED
        self.SMTP_PORT = 587 # Example with outlook SMTP server port - CAN BE CHANGED
        
In get_website_status.py you need to provide website domain name or IP Address.
