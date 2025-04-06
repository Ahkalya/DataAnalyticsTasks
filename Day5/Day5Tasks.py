# Validate Password
import re
def validatePassword(password):
    pattern =  pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    if re.match(pattern, password):
        print("Password is valid")
    else:
        print("Password is invalid")
        
validatePassword("Hello@123")  
validatePassword("hello123") 

#Validate Url

def validate_Url(url):
    pattern =   pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-z]{2,})(/[^\s]*)?$'
    
    if re.match(pattern, url):
        print("Valid URL")
    else:
        print("Invalid URL")
        
validate_Url("https://www.google.com") 