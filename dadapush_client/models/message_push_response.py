# coding: utf-8

"""
    DaDaPush Public API

    DaDaPush: Real-time Notifications App Send real-time notifications through our API without coding and maintaining your own app for iOS or Android devices.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contacts@dadapush.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MessagePushResponse(object):
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
        'message_id': 'int'
    }

    attribute_map = {
        'message_id': 'messageId'
    }

    def __init__(self, message_id=None):  # noqa: E501
        """MessagePushResponse - a model defined in OpenAPI"""  # noqa: E501

        self._message_id = None
        self.discriminator = None

        self.message_id = message_id

    @property
    def message_id(self):
        """Gets the message_id of this MessagePushResponse.  # noqa: E501


        :return: The message_id of this MessagePushResponse.  # noqa: E501
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this MessagePushResponse.


        :param message_id: The message_id of this MessagePushResponse.  # noqa: E501
        :type: int
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

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
        if not isinstance(other, MessagePushResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
