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


class MessageObject(object):
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
        'actions': 'list[Action]',
        'channel_name': 'str',
        'content': 'str',
        'created_at': 'str',
        'id': 'int',
        'title': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'channel_name': 'channelName',
        'content': 'content',
        'created_at': 'createdAt',
        'id': 'id',
        'title': 'title'
    }

    def __init__(self, actions=None, channel_name=None, content=None, created_at=None, id=None,
                 title=None):  # noqa: E501
        """MessageObject - a model defined in OpenAPI"""  # noqa: E501

        self._actions = None
        self._channel_name = None
        self._content = None
        self._created_at = None
        self._id = None
        self._title = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        self.channel_name = channel_name
        self.content = content
        self.created_at = created_at
        self.id = id
        self.title = title

    @property
    def actions(self):
        """Gets the actions of this MessageObject.  # noqa: E501

        action size range is 0,3  # noqa: E501

        :return: The actions of this MessageObject.  # noqa: E501
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this MessageObject.

        action size range is 0,3  # noqa: E501

        :param actions: The actions of this MessageObject.  # noqa: E501
        :type: list[Action]
        """

        self._actions = actions

    @property
    def channel_name(self):
        """Gets the channel_name of this MessageObject.  # noqa: E501


        :return: The channel_name of this MessageObject.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this MessageObject.


        :param channel_name: The channel_name of this MessageObject.  # noqa: E501
        :type: str
        """
        if channel_name is None:
            raise ValueError("Invalid value for `channel_name`, must not be `None`")  # noqa: E501

        self._channel_name = channel_name

    @property
    def content(self):
        """Gets the content of this MessageObject.  # noqa: E501


        :return: The content of this MessageObject.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MessageObject.


        :param content: The content of this MessageObject.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this MessageObject.  # noqa: E501

        format: yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The created_at of this MessageObject.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MessageObject.

        format: yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param created_at: The created_at of this MessageObject.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this MessageObject.  # noqa: E501


        :return: The id of this MessageObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageObject.


        :param id: The id of this MessageObject.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this MessageObject.  # noqa: E501


        :return: The title of this MessageObject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MessageObject.


        :param title: The title of this MessageObject.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if not isinstance(other, MessageObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
