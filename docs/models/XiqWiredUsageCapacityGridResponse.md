# extremecloudiq.model.xiq_wired_usage_capacity_grid_response.XiqWiredUsageCapacityGridResponse

Response body for Wired Usage and Capacity grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response body for Wired Usage and Capacity grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique device identifier | [optional] value must be a 64 bit integer
**device_hostname** | str,  | str,  | The hostname of the device | [optional] 
**device_ip** | str,  | str,  | The IP address of the device | [optional] 
**is_stack** | bool,  | BoolClass,  | Indicates whether the device is a stack or not | [optional] 
**site** | str,  | str,  | Site location of the device | [optional] 
**building** | str,  | str,  | The building where the device is located | [optional] 
**floor** | str,  | str,  | The floor where the device is located | [optional] 
**total_clients_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clients of the device | [optional] value must be a 64 bit integer
**total_issue_clients_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clients with issues of the device | [optional] value must be a 64 bit integer
**total_bandwidth_utilized** | decimal.Decimal, int,  | decimal.Decimal,  | Total utilized bandwidth in Bytes | [optional] value must be a 64 bit integer
**total_throughput_rx** | decimal.Decimal, int,  | decimal.Decimal,  | Total Rx throughput in packets per second | [optional] value must be a 64 bit integer
**total_throughput_tx** | decimal.Decimal, int,  | decimal.Decimal,  | Total Tx throughput in packets per second | [optional] value must be a 64 bit integer
**total_unicast_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of unicast packets from total number of packets | [optional] value must be a 32 bit integer
**total_multicast_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of multicast packets from total number of packets | [optional] value must be a 32 bit integer
**total_broadcast_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of broadcast packets from total number of packets | [optional] value must be a 32 bit integer
**total_queue_tx_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of transmitted packets on all QOS queues | [optional] value must be a 64 bit integer
**total_queue_congestion_pkts** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of packets dropped due to congestion on all QOS queues | [optional] value must be a 64 bit integer
**total_packets_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unicast, multicast and broadcast packets | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

