# extremecloudiq.model.xiq_network_service_request.XiqNetworkServiceRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The network service name. | [optional] 
**description** | str,  | str,  | The network service name. | [optional] 
**ip_protocol** | [**XiqNetworkIpProtocol**](XiqNetworkIpProtocol.md) | [**XiqNetworkIpProtocol**](XiqNetworkIpProtocol.md) |  | [optional] 
**protocol_number** | decimal.Decimal, int,  | decimal.Decimal,  | The Network Protocol Number | [optional] value must be a 32 bit integer
**port_number** | decimal.Decimal, int,  | decimal.Decimal,  | The Network Port Number | [optional] value must be a 32 bit integer
**alg_type** | [**XiqNetworkAlgType**](XiqNetworkAlgType.md) | [**XiqNetworkAlgType**](XiqNetworkAlgType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

