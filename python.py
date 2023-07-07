# TAKE EMAIL ADDRESS FROM USER
email = input('Enter your email address: ').strip()

#  SLICE AND STORE USERNAME
username = email[:email.index('@')]

# SLICE AND STORE DOMAIN NAME
domain = email[email.index('@')+1:]

# MAKE OUTPUT RESULT USING USERNAME AND DOMAIN NAME
result = "Your username = {}\n Your domain = {}".format(username, domain)

# PRINT THE RESULT
print(result)