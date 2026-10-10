"""Immutable locale/revision contracts shared by legacy and bounded debt repair."""
from dataclasses import dataclass

from portal_extended_locales import ExpansionError, select_locales

QUALITY_POLICY = 'extended-quality-debt-v1'
QUALITY_REVISION = 'cldr48-complete-number-v1'


@dataclass(frozen=True)
class RepairContract:
    locale: str
    policy: str
    revision: str

    def __post_init__(self):
        legacy = (self.locale, self.policy, self.revision) == (
            'fr', 'fr-quantity-fallback-v1', 'fr-space-grouping-quarter-v1')
        quality = (self.policy == QUALITY_POLICY and self.revision == QUALITY_REVISION
                   and select_locales(self.locale) == (self.locale,))
        if not (legacy or quality):
            raise ExpansionError('Unsupported exact locale repair contract')

    @property
    def automatic(self):
        return self.policy == QUALITY_POLICY


LEGACY_FRENCH = RepairContract('fr', 'fr-quantity-fallback-v1', 'fr-space-grouping-quarter-v1')


def quality_contract(locale):
    return RepairContract(locale, QUALITY_POLICY, QUALITY_REVISION)
