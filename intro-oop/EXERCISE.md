# OOP Exercises

## User Class

1. Create a class `User` with the following attributes:

- `name` (str)
- `email` (str)
- `password` (str)
- `verified` (bool)

2. Create a method `get_user` that returns a string representation of the user. The string should be formatted as follows:

```
Name: <name>
Email: <email>
Password: <password>
Verified: <verified>
```

3. Create a method `verify` that sets the `verified` attribute to `True`.

4. Create a method `send_email` that sends an email to the user's email address with the message "Your account has been verified".

> You can use the `send_email` function provided below to simulate sending an email.

```python
def send_email(email, message):
    print(f"Sending email to {email}: {message}")
```

5. Create a method `change_password` that takes a new password as an argument and sets the `password` attribute to the new password.
