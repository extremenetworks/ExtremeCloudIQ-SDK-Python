# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "extremecloudiq-api"
VERSION = "23.4.0.41"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ExtremeCloud IQ API",
    author="Extreme Networks Support",
    author_email="support@extremenetworks.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ExtremeCloud IQ API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501
    """
)
