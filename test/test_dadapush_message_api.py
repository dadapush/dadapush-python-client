# coding: utf-8

"""
    DaDaPush Public API

    DaDaPush: Real-time Notifications App Send real-time notifications through our API without coding and maintaining your own app for iOS or Android devices.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contacts@dadapush.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest
from pprint import pprint

import dadapush_client
from dadapush_client import Configuration, Action
from dadapush_client.rest import ApiException


class TestDaDaPushMessageApi(unittest.TestCase):
    """DaDaPushMessageApi unit test stubs"""

    x_channel_token = 'ct4OXfKOnGi0EdR1kbOrNHt8ehSq71SrmdTMOwZ26NlHToVeeU9u'  # str | see: https://www.dadapush.com/channel/list (optional)

    def setUp(self):
        self.api = dadapush_client.DaDaPushMessageApi(
            dadapush_client.ApiClient(Configuration()))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_message(self):
        """Test case for create_message

        push Message to a Channel  # noqa: E501
        """
        actions = [Action(type="link", name="view", url="https://www.dadapush.com/")]
        body = dadapush_client.MessagePushRequest(title="good news",
                                                  content="Good News! DaDaPush releasing new version",
                                                  need_push=True,
                                                  actions=actions
                                                  )  # MessagePushRequest | body

        try:
            # push Message to a Channel
            api_response = self.api.create_message(body, x_channel_token=self.x_channel_token)
            pprint(api_response)
        except ApiException as e:
            pprint(e)

    def test_delete_message(self):
        """Test case for delete_message

        delete a Channel Message  # noqa: E501
        """
        try:
            # push Message to a Channel
            api_response = self.api.delete_message(message_id=227840, x_channel_token=self.x_channel_token)
            pprint(api_response)
        except ApiException as e:
            pprint(e)

    def test_get_message(self):
        """Test case for get_message

        get a Channel Message  # noqa: E501
        """
        try:
            # push Message to a Channel
            api_response = self.api.get_message(message_id=227840, x_channel_token=self.x_channel_token)
            pprint(api_response)
        except ApiException as e:
            pprint(e)

    def test_get_messages(self):
        """Test case for get_messages

        get Message List  # noqa: E501
        """
        try:
            # push Message to a Channel
            api_response = self.api.get_messages(page=1, page_size=10, x_channel_token=self.x_channel_token)
            pprint(api_response)
        except ApiException as e:
            pprint(e)


if __name__ == '__main__':
    unittest.main()
