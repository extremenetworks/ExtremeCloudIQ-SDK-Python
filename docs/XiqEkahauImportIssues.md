# XiqEkahauImportIssues

Any issues related to the import of this floor, eg: why it failed, why an AP was discarded, etc.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) |  | [optional] 
**background** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) |  | [optional] 
**custom_ap_configurations** | **dict(str, list[XiqEkahauImportIssue])** | If the floor was imported but issues occurred while importing custom AP configurations they will be listed here. | [optional] 
**discarded_aps** | [**dict(str, XiqEkahauImportIssue)**](XiqEkahauImportIssue.md) | If the floor was imported but some of the APs were discarded they will be listed here. | [optional] 
**discarded_walls** | [**dict(str, XiqEkahauImportIssue)**](XiqEkahauImportIssue.md) | If the floor was imported but some of the walls were discarded they will be listed here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


