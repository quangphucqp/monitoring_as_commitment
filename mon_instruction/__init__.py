from otree.api import *
from parameters import Params


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'monitored_instruction'
    players_per_group = None
    num_rounds = 1
    monitor_phone = Params.monitor_phone
    day_in_week = Params.day_in_week


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MonitoringService(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            phone_number=Constants.monitor_phone,
            day_in_week=Constants.day_in_week
        )


class SettingUp(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            phone_number=Constants.monitor_phone
        )


page_sequence = [MonitoringService, SettingUp]
