from setuptools import setup

setup(
    name='webgen',
    version='0.2',
    py_modules=['webgen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
            [console_scripts]
            webgen=webgen:main
        ''',
)
