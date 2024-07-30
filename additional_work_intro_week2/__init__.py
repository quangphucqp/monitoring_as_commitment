from otree.api import *


doc = """
Intro screen of Additional Work Week2
"""


class Constants(BaseConstants):
    name_in_url = 'additional_work_intro_week2'
    players_per_group = None
    num_rounds = 1
    monitored = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Work_Additional_Task(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            allocation_this_week=player.participant.vars['allocation_week2'],
        )


page_sequence = [Work_Additional_Task]
