from setuptools import setup

setup(
    name='employeesInOffice',
    version='1.0.0',
    py_modules=['employees'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        employees=employees:cli
    ''',
)
