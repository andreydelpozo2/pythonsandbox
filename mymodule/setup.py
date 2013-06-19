from distutils.core import setup, Extension

module1 = Extension('spam',
                    sources = ['spam.c'])

setup (name = 'Spam Package',
       version = '1.0',
       description = 'This is a lot of spam',
       ext_modules = [module1])