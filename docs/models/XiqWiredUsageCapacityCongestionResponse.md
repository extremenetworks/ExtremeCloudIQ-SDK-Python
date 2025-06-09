# extremecloudiq.model.xiq_wired_usage_capacity_congestion_response.XiqWiredUsageCapacityCongestionResponse

Response body for Wired Usage and Capacity - Wired Congestion widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response body for Wired Usage and Capacity - Wired Congestion widget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_queue_tx_packets** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of transmitted packets on all QOS queues | [optional] value must be a 64 bit integer
**total_queue_congestion_packets** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of packets dropped due to congestion on all QOS queues | [optional] value must be a 64 bit integer
**total_congestion_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of packets dropped due to congestion vs total number of transmitted packets on all QOS queues | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

