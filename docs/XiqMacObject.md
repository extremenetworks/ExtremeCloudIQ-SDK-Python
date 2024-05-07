# XiqMacObject

The MAC Object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The MAC object name | [optional] 
**description** | **str** | The MAC object description. | [optional] 
**predefined** | **bool** | Whether the MAC Oui is predefined | [optional] 
**value** | **str** | The MAC octets. | [optional] 
**mac_type** | [**XiqMacObjectType**](XiqMacObjectType.md) |  | [optional] 
**defender_defined** | **bool** | Whether defender is defined | [optional] 
**mac_address_end** | **str** | The MAC address end, only available for \&quot;MAC_RANGE\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


