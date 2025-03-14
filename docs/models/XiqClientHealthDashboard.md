# extremecloudiq.model.xiq_client_health_dashboard.XiqClientHealthDashboard

The client health diagnostic data for total clients, unhealthy clients, wired, and wireless unhealthy clients.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The client health diagnostic data for total clients, unhealthy clients, wired, and wireless unhealthy clients. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_clients** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of clients | [optional] value must be a 64 bit integer
**total_unhealthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of unhealthy clients | [optional] value must be a 64 bit integer
**wired_unhealthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wired unhealthy clients | [optional] value must be a 64 bit integer
**wireless_unhealthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wireless unhealthy clients | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

