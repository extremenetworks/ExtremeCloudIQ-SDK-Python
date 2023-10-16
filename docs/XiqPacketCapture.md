# XiqPacketCapture

This represents the packet capture session
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | [optional] 
**start_time** | **datetime** | The packet capture start time | [optional] 
**end_time** | **datetime** | The packet capture end time | [optional] 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The packet capture session name. If the name is null or empty, it will be auto generated. | [optional] 
**duration** | **int** | An integer containing the set packet capture duration in seconds, from 5 to a maximum of 604800 seconds (1 week). If duration is set to 0 or unspecified, capture stops when platform-maximum size is reached. | [optional] 
**capture_id_type** | [**XiqCaptureIdentifierType**](XiqCaptureIdentifierType.md) |  | [optional] 
**ap_serial_number** | **str** | The globally unique serial number of the device being registered. The serial number is represented as a string. | [optional] 
**device_ids** | **list[int]** | The device ID list. | [optional] 
**location_id** | **int** | The assigned location ID, it must be FLOOR type | [optional] 
**destination** | [**XiqDestinationType**](XiqDestinationType.md) |  | [optional] 
**filter** | [**XiqCaptureFilter**](XiqCaptureFilter.md) |  | [optional] 
**capture_if** | [**XiqCaptureLocation**](XiqCaptureLocation.md) |  | [optional] 
**status** | [**XiqPacketCaptureStatus**](XiqPacketCaptureStatus.md) |  | [optional] 
**results** | [**list[XiqCaptureResult]**](XiqCaptureResult.md) | The list of packet capture results - a PacketCaptureResult for each device&#39;s interface | [optional] 
**cloud_storage** | **str** | XIQ cloud storage location for the archive of all capture files in this capture session, if available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


