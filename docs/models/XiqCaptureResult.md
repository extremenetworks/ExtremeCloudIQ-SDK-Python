# extremecloudiq.model.xiq_capture_result.XiqCaptureResult

This represents the packet capture result on an AP's interface. A packet capture session may involve multiple APs on multiple interfaces.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This represents the packet capture result on an AP&#x27;s interface. A packet capture session may involve multiple APs on multiple interfaces. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | [optional] value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**start_time** | str, datetime,  | str,  | The packet capture start time | [optional] value must conform to RFC-3339 date-time
**end_time** | str, datetime,  | str,  | The packet capture end time | [optional] value must conform to RFC-3339 date-time
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device identifier | [optional] value must be a 64 bit integer
**hostname** | str,  | str,  | The device host name | [optional] 
**mac_address** | str,  | str,  | The device MAC address | [optional] 
**interface_name** | str,  | str,  | The interface name such as \&quot;WIFI0\&quot;, \&quot;WIFI1\&quot;, \&quot;ETH0\&quot;, etc. | [optional] 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID | [optional] value must be a 64 bit integer
**[locations](#locations)** | list, tuple,  | tuple,  | The detailed location | [optional] 
**status** | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) |  | [optional] 
**error_message** | str,  | str,  | The error message (may be empty). | [optional] 
**storage** | [**XiqStorage**](XiqStorage.md) | [**XiqStorage**](XiqStorage.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

The detailed location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The detailed location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

