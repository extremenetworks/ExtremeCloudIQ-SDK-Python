from extremecloudiq.paths.deployments_deployment_id.get import ApiForget
from extremecloudiq.paths.deployments_deployment_id.put import ApiForput
from extremecloudiq.paths.deployments_deployment_id.delete import ApiFordelete


class DeploymentsDeploymentId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
