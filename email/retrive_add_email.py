

def retrive_emails():
    
    emails = open("email_address")
    email_list = []

    for email in emails:
        email_list.append(email)
    
    return email_list