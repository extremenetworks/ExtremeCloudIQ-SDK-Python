# extremecloudiq.model.xiq_pcg_port_assignment_entry.XiqPcgPortAssignmentEntry

The PCG port assignment entry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The PCG port assignment entry | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID of AP150W or AP302W | value must be a 64 bit integer
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**eth1_user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The eth1 user ID, get available users from \&quot;/pcgs/key-based/network-policy-{policyId}/users\&quot; | [optional] value must be a 64 bit integer
**eth2_user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The eth2 user ID, get available users from \&quot;/pcgs/key-based/network-policy-{policyId}/users\&quot; | [optional] value must be a 64 bit integer
**eth3_user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The eth3 user ID, get available users from \&quot;/pcgs/key-based/network-policy-{policyId}/users\&quot; | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

