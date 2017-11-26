import setuptools

setuptools.setup(
    name="jweb",
    version="0.1.0",
    url="https://github.com/jinniahn/jweb",

    author="jinsub ahn",
    author_email="jinniahn@gmail.com",

    description="it could control your browser through python",
    long_description=open('README.org').read(),

    packages=setuptools.find_packages(),

    entry_points = {
        'console_scripts': ['js-runner=jweb.jsrunner:main']
    },

    package_data={'jweb': ['data/*.js']},

    install_requires=[
        'rpyc', 'selenium'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
