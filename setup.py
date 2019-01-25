import setuptools

setuptools.setup(
    name="fogstream-cli",
    version="0.0.1",
    author="Dmitry Kotov",
    author_email="dmitrii.kotov@fogstream.com",
    description="Fogstream CLI",
    long_description="Fogstream CLI",
    packages=setuptools.find_packages(),
    url='https://github.com/fogstream/fogstream-cli',
    entry_points={
        'console_scripts': ['fogstream-cli=fogstream_cli.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    install_required=[
        'GitPython==2.1.11',
        'Jinja2==2.10',
        'Click==7.0'
    ]
)