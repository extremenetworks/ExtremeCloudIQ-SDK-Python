# extremecloudiq.model.xiq_hotspot_connection_capability.XiqHotspotConnectionCapability

The connection capability informs client devices about available network services.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The connection capability informs client devices about available network services. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**protocol** | [**XiqHotspotConnectionCapabilityProtocol**](XiqHotspotConnectionCapabilityProtocol.md) | [**XiqHotspotConnectionCapabilityProtocol**](XiqHotspotConnectionCapabilityProtocol.md) |  | 
**port_number** | decimal.Decimal, int,  | decimal.Decimal,  | The port number. | value must be a 32 bit integer
**status** | [**XiqHotspotConnectionCapabilityStatus**](XiqHotspotConnectionCapabilityStatus.md) | [**XiqHotspotConnectionCapabilityStatus**](XiqHotspotConnectionCapabilityStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

