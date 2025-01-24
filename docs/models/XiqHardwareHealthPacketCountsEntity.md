# extremecloudiq.model.xiq_hardware_health_packet_counts_entity.XiqHardwareHealthPacketCountsEntity

ExtremeCloud IQ Data Point

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Data Point | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp | value must be a 64 bit integer
**unicast_tx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unicast Tx | [optional] 
**unicast_rx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unicast Rx | [optional] 
**multicast_tx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Multicast Tx | [optional] 
**multicast_rx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Multicast Rx | [optional] 
**broadcast_tx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Broadcast Tx | [optional] 
**broadcast_rx** | decimal.Decimal, int, float,  | decimal.Decimal,  | Broadcast Rx | [optional] 
**throughput** | decimal.Decimal, int, float,  | decimal.Decimal,  | Throughput | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

