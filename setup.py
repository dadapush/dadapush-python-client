# coding: utf-8

"""
    DaDaPush Public API

    DaDaPush: Real-time Notifications App Send real-time notifications through our API without coding and maintaining your own app for iOS or Android devices.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contacts@dadapush.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dadapush-client"
VERSION = "1.0.0"
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
    description="DaDaPush Public API",
    author_email="contacts@dadapush.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "DaDaPush Public API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    DaDaPush: Real-time Notifications App Send real-time notifications through our API without coding and maintaining your own app for iOS or Android devices.  # noqa: E501
    """
)
