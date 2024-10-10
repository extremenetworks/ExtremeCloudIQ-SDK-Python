# XiqIotProfileThreadGateway

Thread Gateway application settings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_pan_id** | **str** | The Personal Area Network (PAN) ID. (4 hex digits). FFFF is reserved. | 
**ext_pan_id** | **str** | The Extended Personal Area Network (PAN) ID. (16 hex digits) | 
**master_key** | **str** | The network key is used to secure access to the Thread network. It is used to encrypt and authenticate all messages on the network. (32 hex digits) | 
**network_name** | **str** | A human-readable name for the network, up to 16 bytes in length. | 
**channel** | **int** | 802.15.4 channel number, 11-26 | 
**comm_credentials** | **str** | The Commissioner Credential is used along with the Extended PAN ID and Network Name to create the PSKc (Pre-Shared Key for the Commissioner). | [optional] 
**comm_timeout** | **int** | After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days. | [optional] 
**enable_nat64** | **bool** | Enable NAT64 functions including the translator and the prefix publishing. | [optional] 
**enable_dns_search_domain** | **bool** | Enable adding DNS search domain to unqualified host lookups forwarded by upstream DNS (in the thread border router). | [optional] 
**white_list** | [**list[XiqIotpTgWhiteListEntry]**](XiqIotpTgWhiteListEntry.md) |  | [optional] 
**default_user_profile_id** | **int** | The default user-profile ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


