from extremecloudiq.paths.ccgs_id.get import ApiForget
from extremecloudiq.paths.ccgs_id.put import ApiForput
from extremecloudiq.paths.ccgs_id.delete import ApiFordelete


class CcgsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
