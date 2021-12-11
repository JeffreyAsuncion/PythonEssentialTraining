#!/home/jepoy/anaconda3/bin/python

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count+=1
    if count > max_attempt:
        break # this exits the loop
    if count == 3:
        continue  # this goes to next iteration of loop
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else 'Calling the FBI ...')
    
