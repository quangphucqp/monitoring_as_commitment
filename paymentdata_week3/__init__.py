from otree.api import *

doc = """
Payment Data
"""


class Constants(BaseConstants):
    name_in_url = 'PaymentData'
    players_per_group = None
    num_rounds = 1
    monitored = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    # Personal Details
    personal_code = models.StringField(
        label='Personal Code:',
        widget=widgets.TextInput(),
    )
    iban = models.StringField(
        label='IBAN (International Bank Account Number):',
        widget=widgets.TextInput(),
    )


# PAGES
class PersonalDetails(Page):
    pass

    form_model = 'player'
    form_fields = ['personal_code', 'iban']

class End(Page):
    pass


page_sequence = [PersonalDetails, End]
