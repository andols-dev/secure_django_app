# Django app that creates users and handle logins

The app uses Django's built-in user management tools to create users and handle logins. The app also uses django-axes to protect against brute force attacks by tracking failed login attempts and locking accounts after a certain number of failed attempts. The app uses CSRF protection to protect against CSRF attacks and Django's built-in password hashing to protect passwords. The app uses secure authentication methods to verify the user's credentials. The app also uses django-admin-honeypot.
