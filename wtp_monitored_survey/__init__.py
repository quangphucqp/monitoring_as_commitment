from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'wtp_monitored_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    useful = models.IntegerField(
        label='',
        choices=[
            [0, '0: Not at all useful'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10: Extremely useful']
        ],
        widget=widgets.RadioSelectHorizontal
    )
    accept_if_free = models.BooleanField(
        label='',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelectHorizontal
    )
    wtp_choice_05 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_10 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_15 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_20 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_25 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_30 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_40 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_50 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)
    wtp_choice_60 = models.BooleanField(choices=[[1, ''], [0, '']], widget=widgets.RadioSelectHorizontal)


# PAGES
class WTPMonitored(Page):
    pass

    form_model = 'player'
    form_fields = ['useful', 'accept_if_free', 'wtp_choice_05', 'wtp_choice_10', 'wtp_choice_15', 'wtp_choice_20',
                   'wtp_choice_25', 'wtp_choice_30', 'wtp_choice_40', 'wtp_choice_50', 'wtp_choice_60']


page_sequence = [WTPMonitored]
