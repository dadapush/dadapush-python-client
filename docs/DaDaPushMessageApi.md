# dadapush_client.DaDaPushMessageApi

All URIs are relative to *https://www.dadapush.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message**](DaDaPushMessageApi.md#create_message) | **POST** /api/v1/message | push Message to a Channel
[**delete_message**](DaDaPushMessageApi.md#delete_message) | **DELETE** /api/v1/message/{messageId} | delete a Channel Message
[**get_message**](DaDaPushMessageApi.md#get_message) | **GET** /api/v1/message/{messageId} | get a Channel Message
[**get_messages**](DaDaPushMessageApi.md#get_messages) | **GET** /api/v1/messages | get Message List


# **create_message**
> ResultOfMessagePushResponse create_message(body, x_channel_token=x_channel_token)

push Message to a Channel

<h2>Rate Limit:</h2><ul><li>1 request per 1s</li><li>30 request per 1m</li><li>500 request per 1h</li></ul><h2>Result code/errmsg List:</h2><ul><li>0: ok</li><li>1: server error</li><li>101: channel is exists</li><li>102: channel is not exists</li><li>103: channel token error</li><li>104: channel is not exists</li><li>105: message is not exists</li><li>204: bad request</li><li>205: permission deny</li><li>206: too many request, please after 5 minutes to try!</li><li>301: duplicate username/email</li><li>302: user is not exists</li><li>303: user password is error</li><li>304: client push token is error</li><li>305: user is disabled</li><li>306: your subscription is expired</li><li>307: user not subscribe channel</li></ul>

### Example

```python
from __future__ import print_function
import time
import dadapush_client
from dadapush_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dadapush_client.DaDaPushMessageApi()
body = dadapush_client.MessagePushRequest() # MessagePushRequest | body
x_channel_token = 'x_channel_token_example' # str | see: https://www.dadapush.com/channel/list (optional)

try:
    # push Message to a Channel
    api_response = api_instance.create_message(body, x_channel_token=x_channel_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaDaPushMessageApi->create_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagePushRequest**](MessagePushRequest.md)| body | 
 **x_channel_token** | **str**| see: https://www.dadapush.com/channel/list | [optional] 

### Return type

[**ResultOfMessagePushResponse**](ResultOfMessagePushResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> Result delete_message(message_id, x_channel_token=x_channel_token)

delete a Channel Message

<h2>Rate Limit:</h2><ul><li>10 request per 1s</li><li>100 request per 1m</li><li>1000 request per 1h</li></ul><h2>Result code/errmsg List:</h2><ul><li>0: ok</li><li>1: server error</li><li>101: channel is exists</li><li>102: channel is not exists</li><li>103: channel token error</li><li>104: channel is not exists</li><li>105: message is not exists</li><li>204: bad request</li><li>205: permission deny</li><li>206: too many request, please after 5 minutes to try!</li><li>301: duplicate username/email</li><li>302: user is not exists</li><li>303: user password is error</li><li>304: client push token is error</li><li>305: user is disabled</li><li>306: your subscription is expired</li><li>307: user not subscribe channel</li></ul>

### Example

```python
from __future__ import print_function
import time
import dadapush_client
from dadapush_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dadapush_client.DaDaPushMessageApi()
message_id = 56 # int | messageId
x_channel_token = 'x_channel_token_example' # str | see: https://www.dadapush.com/channel/list (optional)

try:
    # delete a Channel Message
    api_response = api_instance.delete_message(message_id, x_channel_token=x_channel_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaDaPushMessageApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**| messageId | 
 **x_channel_token** | **str**| see: https://www.dadapush.com/channel/list | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message**
> ResultOfMessageObject get_message(message_id, x_channel_token=x_channel_token)

get a Channel Message

<h2>Rate Limit:</h2><ul><li>10 request per 1s</li><li>100 request per 1m</li><li>1000 request per 1h</li></ul><h2>Result code/errmsg List:</h2><ul><li>0: ok</li><li>1: server error</li><li>101: channel is exists</li><li>102: channel is not exists</li><li>103: channel token error</li><li>104: channel is not exists</li><li>105: message is not exists</li><li>204: bad request</li><li>205: permission deny</li><li>206: too many request, please after 5 minutes to try!</li><li>301: duplicate username/email</li><li>302: user is not exists</li><li>303: user password is error</li><li>304: client push token is error</li><li>305: user is disabled</li><li>306: your subscription is expired</li><li>307: user not subscribe channel</li></ul>

### Example

```python
from __future__ import print_function
import time
import dadapush_client
from dadapush_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dadapush_client.DaDaPushMessageApi()
message_id = 56 # int | messageId
x_channel_token = 'x_channel_token_example' # str | see: https://www.dadapush.com/channel/list (optional)

try:
    # get a Channel Message
    api_response = api_instance.get_message(message_id, x_channel_token=x_channel_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaDaPushMessageApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**| messageId | 
 **x_channel_token** | **str**| see: https://www.dadapush.com/channel/list | [optional] 

### Return type

[**ResultOfMessageObject**](ResultOfMessageObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> ResultOfPageResponseOfMessageObject get_messages(page, page_size, x_channel_token=x_channel_token)

get Message List

<h2>Rate Limit:</h2><ul><li>1 request per 1s</li><li>45 request per 1m</li></ul><h2>Result code/errmsg List:</h2><ul><li>0: ok</li><li>1: server error</li><li>101: channel is exists</li><li>102: channel is not exists</li><li>103: channel token error</li><li>104: channel is not exists</li><li>105: message is not exists</li><li>204: bad request</li><li>205: permission deny</li><li>206: too many request, please after 5 minutes to try!</li><li>301: duplicate username/email</li><li>302: user is not exists</li><li>303: user password is error</li><li>304: client push token is error</li><li>305: user is disabled</li><li>306: your subscription is expired</li><li>307: user not subscribe channel</li></ul>

### Example

```python
from __future__ import print_function
import time
import dadapush_client
from dadapush_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dadapush_client.DaDaPushMessageApi()
page = 1 # int | greater than 1 (default to 1)
page_size = 10 # int | range is 1,50 (default to 10)
x_channel_token = 'x_channel_token_example' # str | see: https://www.dadapush.com/channel/list (optional)

try:
    # get Message List
    api_response = api_instance.get_messages(page, page_size, x_channel_token=x_channel_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DaDaPushMessageApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| greater than 1 | [default to 1]
 **page_size** | **int**| range is 1,50 | [default to 10]
 **x_channel_token** | **str**| see: https://www.dadapush.com/channel/list | [optional] 

### Return type

[**ResultOfPageResponseOfMessageObject**](ResultOfPageResponseOfMessageObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

