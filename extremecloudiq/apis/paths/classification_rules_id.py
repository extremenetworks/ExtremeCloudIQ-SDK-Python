from extremecloudiq.paths.classification_rules_id.get import ApiForget
from extremecloudiq.paths.classification_rules_id.put import ApiForput
from extremecloudiq.paths.classification_rules_id.delete import ApiFordelete


class ClassificationRulesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
