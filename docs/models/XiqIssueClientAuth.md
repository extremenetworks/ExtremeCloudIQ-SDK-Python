# extremecloudiq.model.xiq_issue_client_auth.XiqIssueClientAuth

Wireless clients issue authentication

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Wireless clients issue authentication | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date_time** | decimal.Decimal, int,  | decimal.Decimal,  | The time and date when the issue occurred (epoch milliseconds) | [optional] value must be a 64 bit integer
**reason_code** | str,  | str,  | The reason why the problem occurred. | [optional] must be one of ["USER_NOT_FOUND", "INVALID_CREDENTIAL", "INVALID_DOMAIN", "INCORRECT_EAP_TYPE", "INVALID_CERTIFICATE", "RADIUS_SERVER_REJECT", "RADIUS_SERVER_UNREACHABLE", "ACTIVE_DIRECTORY_DOMAIN_NOT_JOINED", "PASSPHRASE_MISMATCH", "PPSK_SESSION_LIMIT_EXCEEDED", "PPSK_MAC_BIND_FAILURE", "USER_PROFILE_NOT_ALLOWED", "INVALID_VLAN_USER_PROFILE_ID", "PPSK_REJECTED_BY_GUEST_ACCESS", "_802_DOT_1X_REJECTED_BY_GUEST_ACCESS", "GUEST_ACCESS_UNREACHABLE", "CLIENT_AP_VLAN_MISMATCH", "PORT_BASED_INTERFACE_CHECK_ISSUE", ] 
**device_name** | str,  | str,  | The device name to which client was connected | [optional] 
**slowness_duration** | decimal.Decimal, int,  | decimal.Decimal,  | auth slow duration in seconds | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

