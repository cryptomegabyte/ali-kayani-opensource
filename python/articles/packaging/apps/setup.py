from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name='add_app',
      version='0.1',
      description='An app that adds!',
      classifiers=[
        'Development Status :: 1.2-Beta',
        'Programming Language :: Python :: 3.10',
        'License ::MIT License',
        'Topic :: Calculator :: Adds numbers',
      ],
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
      include_package_data=True,
      zip_safe=False
)
