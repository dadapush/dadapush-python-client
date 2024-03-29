# coding: utf-8

"""
    DaDaPush Public API

    DaDaPush: Real-time Notifications App Send real-time notifications through our API without coding and maintaining your own app for iOS or Android devices.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contacts@dadapush.com
    Generated by: https://openapi-generator.tech
"""

import pprint

import six


class ResultOfMessageObject(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'int',
        'data': 'MessageObject',
        'errmsg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'errmsg': 'errmsg'
    }

    def __init__(self, code=None, data=None, errmsg=None):  # noqa: E501
        """ResultOfMessageObject - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._data = None
        self._errmsg = None
        self.discriminator = None

        self.code = code
        if data is not None:
            self.data = data
        self.errmsg = errmsg

    @property
    def code(self):
        """Gets the code of this ResultOfMessageObject.  # noqa: E501


        :return: The code of this ResultOfMessageObject.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ResultOfMessageObject.


        :param code: The code of this ResultOfMessageObject.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def data(self):
        """Gets the data of this ResultOfMessageObject.  # noqa: E501


        :return: The data of this ResultOfMessageObject.  # noqa: E501
        :rtype: MessageObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResultOfMessageObject.


        :param data: The data of this ResultOfMessageObject.  # noqa: E501
        :type: MessageObject
        """

        self._data = data

    @property
    def errmsg(self):
        """Gets the errmsg of this ResultOfMessageObject.  # noqa: E501


        :return: The errmsg of this ResultOfMessageObject.  # noqa: E501
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """Sets the errmsg of this ResultOfMessageObject.


        :param errmsg: The errmsg of this ResultOfMessageObject.  # noqa: E501
        :type: str
        """
        if errmsg is None:
            raise ValueError("Invalid value for `errmsg`, must not be `None`")  # noqa: E501

        self._errmsg = errmsg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResultOfMessageObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
