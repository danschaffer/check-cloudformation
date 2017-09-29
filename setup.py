from setuptools import setup

setup(
    name='check_cloudformation',
    description='Checks cloudformation files for standards',
    url='https://github.com/danschaffer/check-cloudformation',
    version='0.0.1',
    author='Dan Schaffer',
    author_email='schafferdan@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[''],
    py_modules=['check_cloudformation'],
    entry_points={
        'console_scripts': ['check-cloudformation = check_cloudformation:check_cloudformation'],
    },
)
