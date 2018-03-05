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

**Usages** :

- Make sure you have node.js installed on your computer (i'm suggest using `nvm`)
- go to `project/` folder
- Using: `npm install` to install all dependencies
- Using: `npm run build` to build all of your js codes

When you try to running development's server using `Fabric` :

```
fab server.run
```

This command will automatically run `npm run build` for you.

**Notes** :

- All of npm and node things, inside `project/`
- You can allowed to modify `package.json` and `webpack.config.js` to fill your needs
- I just put all of js codes, inside `project/assets/js/vue/`

**Refs** :

- https://github.com/ezhome/django-webpack-loader
