"""
--> take a gmail address and add a + and a string before the @ symbol
eg: 
take:
--> dots before @ symbol are ignored
louisa.harutyunyan@gmail.com
lou.is.a.har.t ... @gmail.com
--> uppercase and lower case doesn't matter


Given e-mail of user, determine number of them that are unique.
The rules for the email are the same as just described.

inputs:
    - first line n number of emails
    - next n lines are the emails
        - each email address consists of at least one character before @ symbol
        - before @ symbol can be +, dots, numbers, letters
        - after @ symbol is letters numbers and dots
        - email is not case insensitive
output:
    - number of unique emails
"""

def email_address(emails):
    unique_emails = []
    for email in emails:
        email = email.lower()
        email = email.split('@')
        email[0] = email[0].replace('.', '')
        email[0] = email[0].split('+')[0]
        email = '@'.join(email)
        unique_emails.add(email)
    return len(unique_emails)

def main():
    n = int(input())
    emails = []
    for _ in range(n):
        email = input()
        emails.append(email)
    print(email_address(emails))

if __name__ == "__main__":
    main()