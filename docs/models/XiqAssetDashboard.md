# extremecloudiq.model.xiq_asset_dashboard.XiqAssetDashboard

The asset diagnostic data for total, offline, wired, and wireless offline devices.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The asset diagnostic data for total, offline, wired, and wireless offline devices. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_devices** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of devices | [optional] value must be a 64 bit integer
**total_offline_devices** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of offline devices | [optional] value must be a 64 bit integer
**wired_offline_devices** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wired offline devices | [optional] value must be a 64 bit integer
**wireless_offline_devices** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wireless offline devices | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

