# extremecloudiq.ConfigurationUserManagementApi

All URIs are relative to *http://localhost:8081*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_key_based_pcg_users**](ConfigurationUserManagementApi.md#add_key_based_pcg_users) | **POST** /pcgs/key-based/network-policy-{policyId}/users | Add users to a PCG-enabled network policy
[**assign_ports**](ConfigurationUserManagementApi.md#assign_ports) | **POST** /pcgs/key-based/network-policy-{policyId}/port-assignments | Assign ports to devices in network policy
[**create_end_user**](ConfigurationUserManagementApi.md#create_end_user) | **POST** /endusers | Create an end user
[**create_user_group**](ConfigurationUserManagementApi.md#create_user_group) | **POST** /usergroups | Create user group
[**delete_key_based_pcg_users**](ConfigurationUserManagementApi.md#delete_key_based_pcg_users) | **DELETE** /pcgs/key-based/network-policy-{policyId}/users | Delete users from a PCG-enabled network policy
[**delete_pcg**](ConfigurationUserManagementApi.md#delete_pcg) | **DELETE** /pcgs/key-based/network-policy-{policyId} | Delete Private Client Group from a network policy
[**delete_ssid_user**](ConfigurationUserManagementApi.md#delete_ssid_user) | **DELETE** /endusers/{id} | Delete end user by ID
[**delete_user_group**](ConfigurationUserManagementApi.md#delete_user_group) | **DELETE** /usergroups/{id} | Delete user group by ID
[**email_keys**](ConfigurationUserManagementApi.md#email_keys) | **POST** /pcgs/key-based/network-policy-{policyId}/keys/:email | Send keys to users in network policy via Email
[**generate_keys**](ConfigurationUserManagementApi.md#generate_keys) | **POST** /pcgs/key-based/network-policy-{policyId}/keys/:generate | Generate shared keys for users in network policy
[**get_key_based_pcg_users**](ConfigurationUserManagementApi.md#get_key_based_pcg_users) | **GET** /pcgs/key-based/network-policy-{policyId}/users | Get users for a PCG-enabled network policy
[**get_port_assignments**](ConfigurationUserManagementApi.md#get_port_assignments) | **GET** /pcgs/key-based/network-policy-{policyId}/port-assignments | Get device port assignments in network policy
[**list_email_templates**](ConfigurationUserManagementApi.md#list_email_templates) | **GET** /email-templates | List Email templates
[**list_end_users**](ConfigurationUserManagementApi.md#list_end_users) | **GET** /endusers | List end users
[**list_key_based_private_client_groups**](ConfigurationUserManagementApi.md#list_key_based_private_client_groups) | **GET** /pcgs/key-based | List Key-based Private Client Groups
[**list_sms_templates**](ConfigurationUserManagementApi.md#list_sms_templates) | **GET** /sms-templates | List SMS templates
[**list_user_groups**](ConfigurationUserManagementApi.md#list_user_groups) | **GET** /usergroups | List user groups
[**onboard_key_based_private_client_group**](ConfigurationUserManagementApi.md#onboard_key_based_private_client_group) | **POST** /pcgs/key-based/network-policy-{policyId}/:onboard | Create Key-based PCG in network policy
[**regenerate_end_user_password**](ConfigurationUserManagementApi.md#regenerate_end_user_password) | **POST** /endusers/{id}/:regenerate-password | Regenerate a new password for the end user
[**setup_key_based_private_client_group_network_policy**](ConfigurationUserManagementApi.md#setup_key_based_private_client_group_network_policy) | **POST** /pcgs/key-based | Setup a Key-based Private Client Group
[**update_end_user**](ConfigurationUserManagementApi.md#update_end_user) | **PUT** /endusers/{id} | Update an end user
[**update_key_based_pcg_users**](ConfigurationUserManagementApi.md#update_key_based_pcg_users) | **PUT** /pcgs/key-based/network-policy-{policyId}/users | Replace all users in a PCG-enabled network policy
[**update_user_group**](ConfigurationUserManagementApi.md#update_user_group) | **PUT** /usergroups/{id} | Update user group


# **add_key_based_pcg_users**
> add_key_based_pcg_users(policy_id, xiq_create_key_based_pcg_users_request)

Add users to a PCG-enabled network policy

Add users to a PCG-enabled network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
xiq_create_key_based_pcg_users_request = extremecloudiq.XiqCreateKeyBasedPcgUsersRequest() # XiqCreateKeyBasedPcgUsersRequest | The payload of add users to PCG-enabled network policy

    try:
        # Add users to a PCG-enabled network policy
        api_instance.add_key_based_pcg_users(policy_id, xiq_create_key_based_pcg_users_request)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->add_key_based_pcg_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **xiq_create_key_based_pcg_users_request** | [**XiqCreateKeyBasedPcgUsersRequest**](XiqCreateKeyBasedPcgUsersRequest.md)| The payload of add users to PCG-enabled network policy | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_ports**
> XiqPcgAssignPortsResponse assign_ports(policy_id, xiq_pcg_assign_ports_request)

Assign ports to devices in network policy

Assign ports for devices (only support AP150W now) in a network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
xiq_pcg_assign_ports_request = extremecloudiq.XiqPcgAssignPortsRequest() # XiqPcgAssignPortsRequest | The payload of assign ports for devices

    try:
        # Assign ports to devices in network policy
        api_response = api_instance.assign_ports(policy_id, xiq_pcg_assign_ports_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->assign_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **xiq_pcg_assign_ports_request** | [**XiqPcgAssignPortsRequest**](XiqPcgAssignPortsRequest.md)| The payload of assign ports for devices | 

### Return type

[**XiqPcgAssignPortsResponse**](XiqPcgAssignPortsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_end_user**
> XiqEndUser create_end_user(xiq_create_end_user_request)

Create an end user

Create a new end user.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    xiq_create_end_user_request = extremecloudiq.XiqCreateEndUserRequest() # XiqCreateEndUserRequest | Create end user request body

    try:
        # Create an end user
        api_response = api_instance.create_end_user(xiq_create_end_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->create_end_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_end_user_request** | [**XiqCreateEndUserRequest**](XiqCreateEndUserRequest.md)| Create end user request body | 

### Return type

[**XiqEndUser**](XiqEndUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group**
> XiqUserGroup create_user_group(xiq_create_user_group_request)

Create user group

Create a new user group.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    xiq_create_user_group_request = extremecloudiq.XiqCreateUserGroupRequest() # XiqCreateUserGroupRequest | Create user group request body

    try:
        # Create user group
        api_response = api_instance.create_user_group(xiq_create_user_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->create_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_create_user_group_request** | [**XiqCreateUserGroupRequest**](XiqCreateUserGroupRequest.md)| Create user group request body | 

### Return type

[**XiqUserGroup**](XiqUserGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_based_pcg_users**
> delete_key_based_pcg_users(policy_id, xiq_delete_key_based_pcg_users_request)

Delete users from a PCG-enabled network policy

Delete users from a PCG-enabled network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
xiq_delete_key_based_pcg_users_request = extremecloudiq.XiqDeleteKeyBasedPcgUsersRequest() # XiqDeleteKeyBasedPcgUsersRequest | The payload of delete Key-based PCG users request

    try:
        # Delete users from a PCG-enabled network policy
        api_instance.delete_key_based_pcg_users(policy_id, xiq_delete_key_based_pcg_users_request)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->delete_key_based_pcg_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **xiq_delete_key_based_pcg_users_request** | [**XiqDeleteKeyBasedPcgUsersRequest**](XiqDeleteKeyBasedPcgUsersRequest.md)| The payload of delete Key-based PCG users request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pcg**
> delete_pcg(policy_id, ids)

Delete Private Client Group from a network policy

Delete Private Client Group settings from a network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
ids = [56] # list[int] | The IDs of the Key-based PCG entity to be deleted from network policy

    try:
        # Delete Private Client Group from a network policy
        api_instance.delete_pcg(policy_id, ids)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->delete_pcg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **ids** | [**list[int]**](int.md)| The IDs of the Key-based PCG entity to be deleted from network policy | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssid_user**
> delete_ssid_user(id)

Delete end user by ID

Delete a specific end user.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    id = 56 # int | The end user ID

    try:
        # Delete end user by ID
        api_instance.delete_ssid_user(id)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->delete_ssid_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The end user ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> delete_user_group(id)

Delete user group by ID

Delete the user-group for the specified ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    id = 56 # int | The user group ID

    try:
        # Delete user group by ID
        api_instance.delete_user_group(id)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->delete_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user group ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_keys**
> email_keys(policy_id, user_ids)

Send keys to users in network policy via Email

Send keys to specified users in PCG-enabled network policy via Email.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
user_ids = [56] # list[int] | The user IDs

    try:
        # Send keys to users in network policy via Email
        api_instance.email_keys(policy_id, user_ids)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->email_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **user_ids** | [**list[int]**](int.md)| The user IDs | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_keys**
> generate_keys(policy_id, user_ids)

Generate shared keys for users in network policy

Generate/regenerate shared keys for specified users in a specific PCG-enable network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
user_ids = [56] # list[int] | The user IDs

    try:
        # Generate shared keys for users in network policy
        api_instance.generate_keys(policy_id, user_ids)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->generate_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **user_ids** | [**list[int]**](int.md)| The user IDs | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_based_pcg_users**
> list[XiqKeyBasedPcgUser] get_key_based_pcg_users(policy_id)

Get users for a PCG-enabled network policy

Get users for a specific PCG-enabled network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID

    try:
        # Get users for a PCG-enabled network policy
        api_response = api_instance.get_key_based_pcg_users(policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->get_key_based_pcg_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 

### Return type

[**list[XiqKeyBasedPcgUser]**](XiqKeyBasedPcgUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_assignments**
> XiqGetPortAssignmentDetailsResponse get_port_assignments(policy_id)

Get device port assignments in network policy

Get port assignments for devices (only support AP150W now) in a network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID

    try:
        # Get device port assignments in network policy
        api_response = api_instance.get_port_assignments(policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->get_port_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 

### Return type

[**XiqGetPortAssignmentDetailsResponse**](XiqGetPortAssignmentDetailsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_email_templates**
> list[XiqEmailTemplate] list_email_templates(password_type=password_type)

List Email templates

List all Email notification templates.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    password_type = extremecloudiq.XiqPasswordType() # XiqPasswordType | The password type (optional)

    try:
        # List Email templates
        api_response = api_instance.list_email_templates(password_type=password_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->list_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_type** | [**XiqPasswordType**](.md)| The password type | [optional] 

### Return type

[**list[XiqEmailTemplate]**](XiqEmailTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_end_users**
> PagedXiqEndUser list_end_users(page=page, limit=limit, user_group_ids=user_group_ids, usernames=usernames)

List end users

List a page of end users.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
user_group_ids = [56] # list[int] | The user group IDs (optional)
usernames = ['usernames_example'] # list[str] | The list of username (optional)

    try:
        # List end users
        api_response = api_instance.list_end_users(page=page, limit=limit, user_group_ids=user_group_ids, usernames=usernames)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->list_end_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **user_group_ids** | [**list[int]**](int.md)| The user group IDs | [optional] 
 **usernames** | [**list[str]**](str.md)| The list of username | [optional] 

### Return type

[**PagedXiqEndUser**](PagedXiqEndUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_based_private_client_groups**
> list[XiqKeyBasedPcg] list_key_based_private_client_groups()

List Key-based Private Client Groups

List all Key-based Private Client Groups.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    
    try:
        # List Key-based Private Client Groups
        api_response = api_instance.list_key_based_private_client_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->list_key_based_private_client_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[XiqKeyBasedPcg]**](XiqKeyBasedPcg.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sms_templates**
> list[XiqSmsTemplate] list_sms_templates(password_type=password_type)

List SMS templates

List all SMS notification templates.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    password_type = extremecloudiq.XiqPasswordType() # XiqPasswordType | The password type (optional)

    try:
        # List SMS templates
        api_response = api_instance.list_sms_templates(password_type=password_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->list_sms_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_type** | [**XiqPasswordType**](.md)| The password type | [optional] 

### Return type

[**list[XiqSmsTemplate]**](XiqSmsTemplate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> PagedXiqUserGroup list_user_groups(page=page, limit=limit, password_db_location=password_db_location, password_type=password_type)

List user groups

List a page of user groups.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    page = 1 # int | Page number, min = 1 (optional) (default to 1)
limit = 10 # int | Page Size, min = 1, max = 100 (optional) (default to 10)
password_db_location = extremecloudiq.XiqPasswordDbLocation() # XiqPasswordDbLocation | The password DB location (optional)
password_type = extremecloudiq.XiqPasswordType() # XiqPasswordType | The password type (optional)

    try:
        # List user groups
        api_response = api_instance.list_user_groups(page=page, limit=limit, password_db_location=password_db_location, password_type=password_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->list_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, min &#x3D; 1 | [optional] [default to 1]
 **limit** | **int**| Page Size, min &#x3D; 1, max &#x3D; 100 | [optional] [default to 10]
 **password_db_location** | [**XiqPasswordDbLocation**](.md)| The password DB location | [optional] 
 **password_type** | [**XiqPasswordType**](.md)| The password type | [optional] 

### Return type

[**PagedXiqUserGroup**](PagedXiqUserGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_key_based_private_client_group**
> onboard_key_based_private_client_group(policy_id, xiq_onboard_key_based_pcg_request)

Create Key-based PCG in network policy

Create a Key-based Private Client Group for a specific network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
xiq_onboard_key_based_pcg_request = extremecloudiq.XiqOnboardKeyBasedPcgRequest() # XiqOnboardKeyBasedPcgRequest | 

    try:
        # Create Key-based PCG in network policy
        api_instance.onboard_key_based_private_client_group(policy_id, xiq_onboard_key_based_pcg_request)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->onboard_key_based_private_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **xiq_onboard_key_based_pcg_request** | [**XiqOnboardKeyBasedPcgRequest**](XiqOnboardKeyBasedPcgRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_end_user_password**
> XiqRegenerateEndUserPasswordResponse regenerate_end_user_password(id)

Regenerate a new password for the end user

Update the user's password with a system generated password.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    id = 56 # int | The enduser's ID

    try:
        # Regenerate a new password for the end user
        api_response = api_instance.regenerate_end_user_password(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->regenerate_end_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The enduser&#39;s ID | 

### Return type

[**XiqRegenerateEndUserPasswordResponse**](XiqRegenerateEndUserPasswordResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_key_based_private_client_group_network_policy**
> setup_key_based_private_client_group_network_policy(xiq_init_key_based_pcg_network_policy_request)

Setup a Key-based Private Client Group

Setup a Key-based Private Client Group, including network policy, user, user group, SSID, etc.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    xiq_init_key_based_pcg_network_policy_request = extremecloudiq.XiqInitKeyBasedPcgNetworkPolicyRequest() # XiqInitKeyBasedPcgNetworkPolicyRequest | The request to setup Key-based PCG network policy

    try:
        # Setup a Key-based Private Client Group
        api_instance.setup_key_based_private_client_group_network_policy(xiq_init_key_based_pcg_network_policy_request)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->setup_key_based_private_client_group_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xiq_init_key_based_pcg_network_policy_request** | [**XiqInitKeyBasedPcgNetworkPolicyRequest**](XiqInitKeyBasedPcgNetworkPolicyRequest.md)| The request to setup Key-based PCG network policy | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_end_user**
> XiqEndUser update_end_user(id, xiq_update_end_user_request)

Update an end user

Update a specific end user.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    id = 56 # int | The end user ID
xiq_update_end_user_request = extremecloudiq.XiqUpdateEndUserRequest() # XiqUpdateEndUserRequest | Update end user request body

    try:
        # Update an end user
        api_response = api_instance.update_end_user(id, xiq_update_end_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->update_end_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The end user ID | 
 **xiq_update_end_user_request** | [**XiqUpdateEndUserRequest**](XiqUpdateEndUserRequest.md)| Update end user request body | 

### Return type

[**XiqEndUser**](XiqEndUser.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_based_pcg_users**
> update_key_based_pcg_users(policy_id, xiq_update_key_based_pcg_users_request)

Replace all users in a PCG-enabled network policy

Replace all users in a specific PCG-enabled network policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    policy_id = 56 # int | The network policy ID
xiq_update_key_based_pcg_users_request = extremecloudiq.XiqUpdateKeyBasedPcgUsersRequest() # XiqUpdateKeyBasedPcgUsersRequest | The payload of update Key-based PCG users request

    try:
        # Replace all users in a PCG-enabled network policy
        api_instance.update_key_based_pcg_users(policy_id, xiq_update_key_based_pcg_users_request)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->update_key_based_pcg_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The network policy ID | 
 **xiq_update_key_based_pcg_users_request** | [**XiqUpdateKeyBasedPcgUsersRequest**](XiqUpdateKeyBasedPcgUsersRequest.md)| The payload of update Key-based PCG users request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> XiqUserGroup update_user_group(id, xiq_update_user_group_request)

Update user group

Update existing user group information.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import extremecloudiq
from extremecloudiq.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8081
# See configuration.py for a list of all supported configuration parameters.
configuration = extremecloudiq.Configuration(
    host = "http://localhost:8081"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = extremecloudiq.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with extremecloudiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = extremecloudiq.ConfigurationUserManagementApi(api_client)
    id = 56 # int | The user group ID.
xiq_update_user_group_request = extremecloudiq.XiqUpdateUserGroupRequest() # XiqUpdateUserGroupRequest | Update user-group request body

    try:
        # Update user group
        api_response = api_instance.update_user_group(id, xiq_update_user_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationUserManagementApi->update_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user group ID. | 
 **xiq_update_user_group_request** | [**XiqUpdateUserGroupRequest**](XiqUpdateUserGroupRequest.md)| Update user-group request body | 

### Return type

[**XiqUserGroup**](XiqUserGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

