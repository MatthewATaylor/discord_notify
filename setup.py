from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="discord_notify",
    version="0.0.1",
    description="A Discord bot wrapper for easily sending messages to a channel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatthewATaylor/discord_notify",
    author="Matthew Taylor",
    author_email="matthewalantaylor2@gmail.com",
    license="MIT",
    packages=["discord_notify"]
)
