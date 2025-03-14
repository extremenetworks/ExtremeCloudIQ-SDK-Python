# extremecloudiq.model.xiq_site_dashboard_response.XiqSiteDashboardResponse

The diagnostics information for each site.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The diagnostics information for each site. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**site_name** | str,  | str,  | The name of the site with diagnostics | [optional] 
**building_name** | str,  | str,  | The name of the building with diagnostics | [optional] 
**floor_name** | str,  | str,  | The name of the floor with diagnostics | [optional] 
**alert_dashboard** | [**XiqAlertDashboard**](XiqAlertDashboard.md) | [**XiqAlertDashboard**](XiqAlertDashboard.md) |  | [optional] 
**asset_dashboard** | [**XiqAssetDashboard**](XiqAssetDashboard.md) | [**XiqAssetDashboard**](XiqAssetDashboard.md) |  | [optional] 
**client_health_dashboard** | [**XiqClientHealthDashboard**](XiqClientHealthDashboard.md) | [**XiqClientHealthDashboard**](XiqClientHealthDashboard.md) |  | [optional] 
**device_health_dashboard** | [**XiqDeviceHealthDashboard**](XiqDeviceHealthDashboard.md) | [**XiqDeviceHealthDashboard**](XiqDeviceHealthDashboard.md) |  | [optional] 
**usage_and_capacity_dashboard** | [**XiqUsageAndCapacityDashboard**](XiqUsageAndCapacityDashboard.md) | [**XiqUsageAndCapacityDashboard**](XiqUsageAndCapacityDashboard.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

