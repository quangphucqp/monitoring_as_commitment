from otree.api import *
from parameters import Params


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'version_check'
    players_per_group = None
    num_rounds = 1
    code_version = Params.code_version


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES
class CodeVersion(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            version=Constants.code_version,
        )


page_sequence = [CodeVersion]
