import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regeorg",
    version="2.0.1",
    author="Vlatko Kosturjak",
    author_email="vlatko.kosturjak@gmail.com",
    description="pwn a bastion webserver and create SOCKS proxies through the DMZ. Pivot and pwn.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kost/regeorg",
    packages=setuptools.find_packages(),
    install_requires=[
        "urllib3",
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'reGeorgSocksProxy.py'
    ]
)
