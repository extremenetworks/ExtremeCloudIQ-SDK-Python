# extremecloudiq.model.xiq_hotspot_qos_dscp_exception.XiqHotspotQosDscpException

The list of exceptions to the mapping of ah-class to DSCP values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of exceptions to the mapping of ah-class to DSCP values. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dscp_value** | decimal.Decimal, int,  | decimal.Decimal,  | Value for DSCP range. | value must be a 32 bit integer
**ah_class** | decimal.Decimal, int,  | decimal.Decimal,  | Extreme QoS class value. | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

