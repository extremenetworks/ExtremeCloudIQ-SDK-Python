# XiqUpdateRadiusProxyRequest

The payload to update RADIUS proxy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The RADIUS proxy name | [optional] 
**description** | **str** | The RADIUS proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | [optional] 
**retry_count** | **int** | The retry count of RADIUS proxy | [optional] 
**retry_delay** | **int** | The retry delay of RADIUS proxy | [optional] 
**dead_time** | **int** | The dead time of RADIUS proxy | [optional] 
**enable_inject_operator_name_attribute** | **bool** | The flag for enable inject operator name attribute | [optional] 
**clients** | [**list[XiqUpdateRadiusClient]**](XiqUpdateRadiusClient.md) | The RADIUS clients of RADIUS proxy | [optional] 
**realms** | [**list[XiqUpdateRadiusProxyRealm]**](XiqUpdateRadiusProxyRealm.md) | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#39;DEFAULT&#39; and &#39;NULL&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


