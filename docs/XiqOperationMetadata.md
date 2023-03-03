# XiqOperationMetadata

The metadata of Long Running Operation (LRO)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**XiqOperationStatus**](XiqOperationStatus.md) |  | 
**cancelable** | **bool** | Indicates if the operation can be canceled in the current status | 
**percentage** | **int** | The progress in percentage ranges from 0 to 100 (it&#39;s not guaranteed to be accurate) | [optional] 
**step** | **str** | The optional step name for multiple steps operations when the operation is running | [optional] 
**create_time** | **datetime** | The operation&#39;s create time, which is the time when the operation is in PENDING status | 
**update_time** | **datetime** | The operation&#39;s last update time | 
**start_time** | **datetime** | The operation&#39;s start time, which is the time when the operation is in RUNNING status | [optional] 
**end_time** | **datetime** | The operation&#39;s end time, which is the time when the operation is done | [optional] 
**expires_in** | **int** | The number of seconds remaining until the operation expires and is to be deleted. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


