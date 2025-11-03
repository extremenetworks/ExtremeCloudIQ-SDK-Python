# extremecloudiq.model.xiq_wired_queue_stats.XiqWiredQueueStats

QOS queue statistics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | QOS queue statistics | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qos_queue** | decimal.Decimal, int,  | decimal.Decimal,  | QOS queue value | [optional] value must be a 64 bit integer
**cong_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | Number of packets dropped due to congestion on the QOS queue | [optional] value must be a 64 bit integer
**tx_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | Number of packets transmitted on the QOS queue | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

