# extremecloudiq.model.xiq_packet_capture.XiqPacketCapture

This represents the packet capture session

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This represents the packet capture session | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | [optional] value must be a 64 bit integer
**start_time** | str, datetime,  | str,  | The packet capture start time | [optional] value must conform to RFC-3339 date-time
**end_time** | str, datetime,  | str,  | The packet capture end time | [optional] value must conform to RFC-3339 date-time
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The packet capture session name. If the name is null or empty, it will be auto generated. | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | An integer containing the set packet capture duration in seconds, from 5 to a maximum of 604800 seconds (1 week). If duration is set to 0 or unspecified, capture stops when platform-maximum size is reached. | [optional] value must be a 32 bit integer
**capture_id_type** | [**XiqCaptureIdentifierType**](XiqCaptureIdentifierType.md) | [**XiqCaptureIdentifierType**](XiqCaptureIdentifierType.md) |  | [optional] 
**ap_serial_number** | str,  | str,  | The globally unique serial number of the device being registered. The serial number is represented as a string. | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The device ID list. | [optional] 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned location ID, it must be FLOOR type | [optional] value must be a 64 bit integer
**destination** | [**XiqDestinationType**](XiqDestinationType.md) | [**XiqDestinationType**](XiqDestinationType.md) |  | [optional] 
**filter** | [**XiqCaptureFilter**](XiqCaptureFilter.md) | [**XiqCaptureFilter**](XiqCaptureFilter.md) |  | [optional] 
**capture_if** | [**XiqCaptureLocation**](XiqCaptureLocation.md) | [**XiqCaptureLocation**](XiqCaptureLocation.md) |  | [optional] 
**status** | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) |  | [optional] 
**[results](#results)** | list, tuple,  | tuple,  | The list of packet capture results - a PacketCaptureResult for each device&#x27;s interface | [optional] 
**cloud_storage** | str,  | str,  | XIQ cloud storage location for the archive of all capture files in this capture session, if available. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The device ID list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device ID list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The device ID list. | value must be a 64 bit integer

# results

The list of packet capture results - a PacketCaptureResult for each device's interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of packet capture results - a PacketCaptureResult for each device&#x27;s interface | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqCaptureResult**](XiqCaptureResult.md) | [**XiqCaptureResult**](XiqCaptureResult.md) | [**XiqCaptureResult**](XiqCaptureResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

