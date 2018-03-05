# base-django
Base configuration and structure when working with Django Web Framework.  Now,
i'm just using Django 2.x version.

# Python Version

Recommended: `>= 3.6.x`

# Django Version

Recommended: `>= 2.x.x`

# Dependency Tools

- Automate Tasks: Fabric
- Environment variables: django-dotenv
- Debugging: Django Debug Toolbar
- Fake data for test: Faker

## Environment Variable

Please copy and rename `env.sample` to `.env` and update all values based
on your needs.

## Vue.js Integration

By default, this skeleton integrated with Vue.js.  I'm using `django-webpack-loader`
to manage all webpack things.  If you want to integrate with Angular or React, just
modify `webpack.config.js`.

I'm also provide an example for the vue.js `Single File Component`, just run the server
and point your browser to `/welcome`.
