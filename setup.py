from setuptools import setup, find_packages

setup(
    name="war-tactics",
    version="0.1.0",
    author="Tom Ped",
    maintainer="Tom Ped",
    scripts=["bin/war"],
    maintainer_email="",
    url="github.com/tomped/war-tactics",
    description="",
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={"dev": ["black", "nose2", "nose2[coverage_plugin]"]},
)
