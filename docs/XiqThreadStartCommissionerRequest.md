# XiqThreadStartCommissionerRequest

The request to start the thread commissioner on an iot interface of a device.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | The device id | 
**comm_timeout** | **int** | After this timeout the Commissioner will shutdown. The default is 120 sec. but the max is approximately 23 days. | [optional] 
**interface_name** | **str** | The IoT interface on which to start the Commissioner. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


