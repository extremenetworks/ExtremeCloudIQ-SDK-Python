# extremecloudiq.model.xiq_wired_usage_capacity_throughput_response.XiqWiredUsageCapacityThroughputResponse

Response body for Wired Usage and Capacity - Wired Throughput widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response body for Wired Usage and Capacity - Wired Throughput widget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_packets_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of packets | [optional] value must be a 64 bit integer
**unicast_utilization_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of unicast packets from total number of packets | [optional] value must be a 32 bit integer
**multicast_utilization_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of multicast packets from total number of packets | [optional] value must be a 32 bit integer
**broadcast_utilization_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of broadcast packets from total number of packets | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

