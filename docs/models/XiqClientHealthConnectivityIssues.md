# extremecloudiq.model.xiq_client_health_connectivity_issues.XiqClientHealthConnectivityIssues

Wireless clients count with connectivity issues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Wireless clients count with connectivity issues | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of clients | [optional] value must be a 64 bit integer
**association_failures** | decimal.Decimal, int,  | decimal.Decimal,  | The number of failed or slow associations (where slow is defined as &gt;&#x3D; 5 seconds) | [optional] value must be a 64 bit integer
**authentication_failures** | decimal.Decimal, int,  | decimal.Decimal,  | The number of failed or slow authentications (where slow is defined as &gt;&#x3D; 5 seconds) | [optional] value must be a 64 bit integer
**ip_address_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of DHCP issues, including private IP address assignments or slow responses (where slow is defined as &gt;&#x3D; 5 seconds) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

