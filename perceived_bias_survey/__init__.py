from otree.api import *
from parameters import Params


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'perceived_bias_survey'
    players_per_group = None
    num_rounds = 1
    restaurant_name = Params.restaurant_name

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    ideal_selfcontrol = models.IntegerField(
        label='Think about what would be the <i>ideal</i> allocation of these certificates for the first and the '
              'second year. From your current perspective, how many of the ten certificates would you <i>ideally</i> '
              'like to use in year 1 as opposed to year 2? (Choose number 1 - 10)',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )
    tempted_selfcontrol = models.IntegerField(
        label='Some people might be tempted to depart from this ideal allocation. For example, there might be '
              'temptation to use up the certificates sooner, and not keep enough for the second year. Or you might be '
              'tempted to keep too many for the second year. If you just gave in to your temptation, how many would you'
              ' use in the first year?',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )
    expected_selfcontrol = models.IntegerField(
        label='Think about both the ideal and the temptation. Based on your most accurate forecast of how you would '
              'actually behave, how many of the nights would you end up using in year 1 as opposed to year 2?',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )


# PAGES
class PerceivedBiasSurvey(Page):
    pass

    form_model = 'player'
    form_fields = ['ideal_selfcontrol', 'tempted_selfcontrol', 'expected_selfcontrol']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            restaurant_name=Constants.restaurant_name
        )


page_sequence = [PerceivedBiasSurvey]
