from extremecloudiq.paths.alert_policies_id.get import ApiForget
from extremecloudiq.paths.alert_policies_id.put import ApiForput
from extremecloudiq.paths.alert_policies_id.delete import ApiFordelete


class AlertPoliciesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
