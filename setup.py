from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="discord_notify",
    version="0.0.5",
    description="A minimal Discord API webhooks wrapper for sending messages to a Discord channel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatthewATaylor/discord_notify",
    author="Matthew Taylor",
    author_email="matthewalantaylor2@gmail.com",
    license="MIT",
    packages=["discord_notify"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Logging",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities"
    ],
    keywords="discord webhooks logging"
)
