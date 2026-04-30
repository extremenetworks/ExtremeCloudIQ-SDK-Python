# extremecloudiq.model.xiq_issue_client_association.XiqIssueClientAssociation

Wireless clients issue association

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Wireless clients issue association | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time and date when the issue when issue occurred in epoch milliseconds | [optional] value must be a 64 bit integer
**reason_code** | str,  | str,  | The reason why the problem occurred. | [optional] must be one of ["MAXIMUM_CLIENT_COUNT_EXCEEDED", "CLIENT_DENIED_BY_SECURITY_POLICY", "CLIENT_CAPABILITIES_MISMATCH", "AUTHENTICATION_ALGORITHM_UNSUPPORTED", ] 
**device_name** | str,  | str,  | The device name to which client was connected | [optional] 
**slowness_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The duration of slowness in seconds | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

