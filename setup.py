from setuptools import setup, find_packages
from dropzone import __version__


setup(
    name="django-dropzone",
    version=__version__,
    url='https://github.com/Rubinous/django-dropzone',
    license='MIT',
    platforms=['OS Independent'],
    description="A simple django widget for dropzone.js.",
    install_requires=[
        'django>=1.8',
    ],
    long_description=open('README.md').read(),
    author='Ats Nisov, Chris Villa',
    author_email='ats.nisov@googlemail.com',
    maintainer='Ats Nisov',
    maintainer_email='ats.nisov@googlemail.com',
    packages=find_packages(),
    package_data={
        'dropzone': [
            'static/*',
            'templates/*',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
