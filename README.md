# Base Django
Base configuration and structure (or skeleton) when working with Django Web Framework.  Now,
i'm just using Django 2.x version.

The purpose of this skeleton is to reduce developer's efforts when they try to create an app,
we should not create and setup from scratch.

I try to setup all common activities like :

- Logging
- Environment variables
- Integration with Twitter Bootstrap
- Integration with Django Debug Toolbar
- Integration with Mailgun as `EmailBackend`
- Faker
- Fabric

---

## Usages

- Clone this repo
- `pipenv shell`
- `pipenv install`
- Setup configurations, copy `env.sample` to `.env`
- Ready to code!

---

## Python Version

Recommended: `>= 3.7.x`

---

## Django Version

Recommended: `>= 2.7.x`

---

## Environment Variable

Please copy and rename `env.sample` to `.env` and update all values based
on your needs.

---

## Memberships

I just added new functionalities for membership activities, they are :

- Register
- Login
- Forget Password
- Reset Code
- Activation

These codes available at `project/memberships` .  You can learn how to manage your application's
module from this app.

---

## Email Using Mailgun

There are two additional configurations :

- MAILGUN_API_KEY
- MAILGUN_DOMAIN

You can get these configurations from your Mailgun's account dashboard.  Get all values
and set in `.env` file.

When you need to send an email you can use this code:

```python
from django.core import mail

conn = mail.get_connection() # Will return custom mail backend instance
mailer = mail.EmailMessage(
    'test subject',
    'test message',
    'testfrom@shell.com',
    ['to@mail.com'],
    connection=conn
)

mailer.send()
```

To send html:

```python
from django.core import mail

conn = mail.get_connection(as_html=True) # Will return custom mail backend instance
mailer = mail.EmailMessage(
    'test subject',
    '<p>test message</p>',
    'testfrom@shell.com',
    ['to@mail.com'],
    connection=conn
)

mailer.send()
```

Or, more simpler way:

```python
from django.core import mail

# will send as text plain
mail.send_mail(
    'test subject',
    'test message',
    'testfrom@shell.com',
    ['to@mail.com']
)

# will send as html
conn = mail.get_connection(as_html=True) # Will return custom mail backend instance

mail.send_mail(
    'test subject',
    '<p>my message</p>',
    'testfrom@shell.com',
    ['to@mail.com'],
    connection=conn
)
```

Ref: [https://docs.djangoproject.com/en/2.0/topics/email/](https://docs.djangoproject.com/en/2.0/topics/email/)
