import re, pyperclip

# The regular expression for finding emails and phone numbers in the buffer.
# Our program will consist of the two regular expressions. The first expression is for finding emails,
# and the second one is for phone numbers. Then our program must take the buffer and edits the text.

# 1) Regular expression for phone numbers
phoneRe = re.compile(r'''
    (\d{3}|\(\d{3}\))? # This part of the number defines the country of this number(like 812 in NN) 
    (\s|-|\.)? # This part defines the separator of the number( like 8-910)
    (\d{3}) # The first three numbers of the phone number (its an important part, so we dont use "?")
    (\s|-|\.) # This part defines the separator of the number( like 8-910 and its an important part, so we dont use "?")
    (\d{4}) # The last four numbers of the phone number
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # This part is also unimportant and it defines the territorial code
''', re.VERBOSE)

# 2) Regular expression for emails
emailRe = re.compile(r''' 
    [a-zA-Z0-9_-]* # This part defines the user's name
    @ # This sign says that we work with email
    [a-zA-Z0-9_-]* # This part definse the email's name(like @mail, @gmail, @yandex)
    \.[a-zA-Z]{2,4} # The part defines the domain name
''', re.VERBOSE)

text = str(pyperclip.paste())

PhonesAndEmailsFromBuffer = []
for phone in phoneRe.findall(text):
    ph = "-".join((phone[0], phone[2], phone[4]))
    if phone[7] != "":
        ph += " ext " + phone[7]
    PhonesAndEmailsFromBuffer.append(ph.strip("-"))

emailsFromBuffer = []
for email in emailRe.findall(text):
    print(email)
    PhonesAndEmailsFromBuffer.append(email)
print(PhonesAndEmailsFromBuffer)

if len(PhonesAndEmailsFromBuffer):
    print("The new buffer is made!")
    pyperclip.copy('\n'.join(PhonesAndEmailsFromBuffer))
else:
    print("Sorry, your buffer didnt have phones and emails :/")

'''
Test text:

(812)-910-4590
812 910 4490  ext 432
915.1234 x  4723

Help with your order: support@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Bulk and special sales questions: sales@nostarch.com
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com
'''