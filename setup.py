from setuptools import setup

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
packages = [
    "nextcord.ext.app_cmd_listener",
]
setup(
    name="nextcord-ext-app-cmd-listener",
    version="2022.04.02",
    description="An nextcord extension that helps you to listen for application commands invoke.",  # noqa: E501
    long_description=open("README.md").read(),
    url="",
    author="MaskDuck",
    license="MIT",
    classifiers=classifiers,
    keywords="nextcord",
    packages=packages,
    long_description_content_type="text/markdown",
    install_requires=["nextcord"],
)