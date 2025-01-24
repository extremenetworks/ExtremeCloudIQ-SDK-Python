# extremecloudiq.model.xiq_iot_profile_thread_gateway.XiqIotProfileThreadGateway

Thread Gateway application settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Thread Gateway application settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ext_pan_id** | str,  | str,  | The Extended Personal Area Network (PAN) ID. (16 hex digits) | 
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | 802.15.4 channel number, 11-26 | value must be a 32 bit integer
**network_name** | str,  | str,  | A human-readable name for the network, up to 16 bytes in length. | 
**short_pan_id** | str,  | str,  | The Personal Area Network (PAN) ID. (4 hex digits). FFFF is reserved. | 
**master_key** | str,  | str,  | The network key is used to secure access to the Thread network. It is used to encrypt and authenticate all messages on the network. (32 hex digits) | 
**comm_credentials** | str,  | str,  | The Commissioner Credential is used along with the Extended PAN ID and Network Name to create the PSKc (Pre-Shared Key for the Commissioner). | [optional] 
**comm_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days. | [optional] value must be a 32 bit integer
**enable_nat64** | bool,  | BoolClass,  | Enable NAT64 functions including the translator and the prefix publishing. | [optional] 
**enable_dns_search_domain** | bool,  | BoolClass,  | Enable adding DNS search domain to unqualified host lookups forwarded by upstream DNS (in the thread border router). | [optional] 
**[white_list](#white_list)** | list, tuple,  | tuple,  |  | [optional] 
**default_user_profile_id** | decimal.Decimal, int,  | decimal.Decimal,  | The default user-profile ID. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# white_list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqIotpTgWhiteListEntry**](XiqIotpTgWhiteListEntry.md) | [**XiqIotpTgWhiteListEntry**](XiqIotpTgWhiteListEntry.md) | [**XiqIotpTgWhiteListEntry**](XiqIotpTgWhiteListEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

