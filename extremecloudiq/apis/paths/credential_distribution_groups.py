from extremecloudiq.paths.credential_distribution_groups.get import ApiForget
from extremecloudiq.paths.credential_distribution_groups.post import ApiForpost
from extremecloudiq.paths.credential_distribution_groups.delete import ApiFordelete


class CredentialDistributionGroups(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
