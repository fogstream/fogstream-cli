import setuptools

setuptools.setup(
    name="fogstream_cli",
    version="0.0.1",
    author="Dmitry Kotov",
    author_email="dmitrii.kotov@fogstream.com",
    description="Fogstream CLI",
    long_description="Fogstream CLI",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['fogstream-cli=fogstream_cli.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Linux",
    ],
    install_required=[
        'GitPython==2.1.11',
        'Jinja2==2.10',
        'Click==7.0'
    ]
)