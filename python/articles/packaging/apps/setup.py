from setuptools import setup

setup(
      name='add_app',
      version='0.1',
      description='An app that adds!',
      url='https://fakeurl.com',
      author='Foo Bar',
      author_email='foo.bar@foo.com',
      license='MIT',
      packages=['add_app'],
      entry_points = {
            'console_scripts': [
                  'add = add_app.cli:main'
            ],
      },
      zip_safe=False
)
