# extremecloudiq.model.xiq_client_chart_roam_details.XiqClientChartRoamDetails

The Client Roam Trail data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Client Roam Trail data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | Client Start trial in epoch format (milliseconds) | [optional] value must be a 64 bit integer
**device_name_from** | str,  | str,  | The Ap name From | [optional] 
**device_name_to** | str,  | str,  | The Ap name To | [optional] 
**device_mac_from** | str,  | str,  | The Ap mac address From | [optional] 
**device_mac_to** | str,  | str,  | The Ap mac address To | [optional] 
**roam_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The roam duration in milliseconds | [optional] value must be a 32 bit integer
**status_action** | str,  | str,  | The Status of roam action (Completed, Failed) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

