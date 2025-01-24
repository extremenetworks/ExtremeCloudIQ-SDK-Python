# extremecloudiq.model.xiq_atp_packet_counts_response.XiqAtpPacketCountsResponse

Copilot Atp Device Packet Counts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Atp Device Packet Counts | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**summary** | str,  | str,  | the anomaly location | [optional] 
**[atp_packet_counts_entities](#atp_packet_counts_entities)** | list, tuple,  | tuple,  | the anomaly device data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# atp_packet_counts_entities

the anomaly device data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly device data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAtpPacketCountsEntity**](XiqAtpPacketCountsEntity.md) | [**XiqAtpPacketCountsEntity**](XiqAtpPacketCountsEntity.md) | [**XiqAtpPacketCountsEntity**](XiqAtpPacketCountsEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

