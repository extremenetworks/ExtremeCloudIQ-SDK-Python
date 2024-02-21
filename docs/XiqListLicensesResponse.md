# XiqListLicensesResponse

The license information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_application** | **bool** | Whether group by application | [optional] 
**application_id** | **str** | Application Id of current group, valid when groupByApplication is true | [optional] 
**application_name** | **str** | Application name of current group, valid when groupByApplication is true | [optional] 
**license_type_count** | **int** | License type count of current group, valid when groupByApplication is true | [optional] 
**license_entitlement_count** | **int** | License entitlement count of current group, valid when groupByApplication is true | [optional] 
**license_types** | [**list[XiqLicenseType]**](XiqLicenseType.md) | License type list | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


