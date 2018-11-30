import os

from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='python-btr',
      version='1.0',
      description='Import .xlsx file of binance order history.',
      long_description=open(README).read(),
      author="Júnior Carvalho",
      author_email="joseadolfojr@gmail.com",
      license="MIT",
      py_modules=['python-btr'],
      zip_safe=False,
      platforms='any',
      install_requires=['xlrd', ],
      tests_require=['pytest', 'pytest-coverage'],
      test_suite='tests',
      include_package_data=True,
      url='', )
