# XiqUpdateL3AddressProfileRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The L3 Address profile name | 
**description** | **str** | The L3 Address profile description | [optional] 
**enable_classification** | **bool** | The flag to enable classification entries on host name address profile | [optional] 
**classified_entries** | [**list[XiqAddressProfileClassifiedEntry]**](XiqAddressProfileClassifiedEntry.md) | The host name address profile classified entries | [optional] 
**ip_address_end** | **str** | The classified entry IP address end, only available for \&quot;IP_RANGE\&quot; address type | [optional] 
**netmask** | **str** | The classified entry IP address end, only available for \&quot;IP_SUBNET\&quot; address type | [optional] 
**wildcard_mask** | **str** | The wildcard address profile mask value, only available for \&quot;WILDCARD\&quot; address type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


