#!/usr/bin/env python3
import zope.interface

from colrev_core.process import PreparationEndpoint
from colrev_core.built_in.prescreen import ScopePrescreenEndpoint 
from colrev_core.process import DefaultSettings
from dacite import from_dict


@zope.interface.implementer(PreparationEndpoint)
class CustomPrepare:

    source_correction_hint = "check with the developer"
    always_apply_changes = True

    def __init__(self, *, SETTINGS):
        self.SETTINGS = from_dict(data_class=DefaultSettings, data=SETTINGS)

    def prepare(cls, PREPARATION, RECORD):

        if "title" in RECORD.data:
            if any(x == RECORD.data['title'].lower() for x in ScopePrescreenEndpoint.title_complementary_materials_keywords):
                RECORD.prescreen_exclude(
                    reason="complementary material"
                )

        if "url" in RECORD.data:
            if 'https://misq.umn.edu/contents-' in RECORD.data['url']:
                RECORD.prescreen_exclude(
                    reason="complementary material"
                )

        return RECORD


if __name__ == "__main__":
    pass
