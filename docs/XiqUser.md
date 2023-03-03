# XiqUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**login_name** | **str** | Login name, i.e. username or login Email | 
**first_name** | **str** | The first name | [optional] 
**last_name** | **str** | The last name, i.e. family name | [optional] 
**display_name** | **str** | The name to display | [optional] 
**phone** | **str** | The Phone Number | [optional] 
**job_title** | **str** | The job title | [optional] 
**locale** | **str** | The locale | [optional] 
**user_role** | [**XiqUserRole**](XiqUserRole.md) |  | [optional] 
**idle_timeout** | **int** | The idle timeout in minutes, the minimum value is 5 minutes and the maximum value is 4 hours | [optional] 
**last_login_time** | **datetime** | The last login time | [optional] 
**org_id** | **int** | The HIQ organization ID if it is HIQ user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


