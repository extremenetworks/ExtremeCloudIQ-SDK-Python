# XiqCaptureResult

This represents the packet capture result on an AP's interface. A packet capture session may involve multiple APs on multiple interfaces.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | [optional] 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**start_time** | **datetime** | The packet capture start time | [optional] 
**end_time** | **datetime** | The packet capture end time | [optional] 
**device_id** | **int** | The device identifier | [optional] 
**hostname** | **str** | The device host name | [optional] 
**mac_address** | **str** | The device MAC address | [optional] 
**interface_name** | **str** | The interface name such as \&quot;WIFI0\&quot;, \&quot;WIFI1\&quot;, \&quot;ETH0\&quot;, etc. | [optional] 
**location_id** | **int** | The location ID | [optional] 
**locations** | [**list[XiqLocationLegend]**](XiqLocationLegend.md) | The detailed location | [optional] 
**status** | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) |  | [optional] 
**error_message** | **str** | The error message (may be empty). | [optional] 
**storage** | [**XiqStorage**](XiqStorage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


