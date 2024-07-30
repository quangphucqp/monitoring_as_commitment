from otree.api import *
from parameters import Params

doc = """
Personal Code for Testing
"""


class Constants(BaseConstants):
    name_in_url = 'test_personalcode'
    players_per_group = None
    num_rounds = 1
    monitored = 1
    irb_number = Params.irb_number



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    # Personal Code
    personal_code = models.StringField(
        label='Please type in your Personal Code:',
        widget=widgets.TextInput(),
    )


# PAGES
class PersonalCode(Page):
    pass

    form_model = 'player'
    form_fields = ['personal_code']

    @staticmethod  # Store "personal code" to be called in later apps
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['personal_code'] = player.personal_code
        player.participant.vars['pause_counter_week2'] = 0
        player.participant.vars['pause_counter_week3'] = 0


page_sequence = [PersonalCode]
