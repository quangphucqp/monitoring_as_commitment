from otree.api import *


doc = """
Sex-Age Survey
"""


class Constants(BaseConstants):
    name_in_url = 'sex_age_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=16, max=99, label='What is your age? Please fill in a number.')
    sex = models.IntegerField(choices=[[1, "Man"],
                                       [2, "Woman"],
                                       [3, "Prefer not to say"],
                                       [4, "Other (you can indicate in next page)"]],
                              widget=widgets.RadioSelect,
                              label='Are you a:'
                              )
    sex_other = models.StringField(blank=True, label="If you chose Other, please indicate. "
                                                     "You can also leave the field empty.")


# PAGES
class SexAgeSurvey(Page):
    pass

    form_model = 'player'
    form_fields = ['age', 'sex']


class SexOther(Page):
    pass

    form_model = 'player'
    form_fields = ['sex_other']

    @staticmethod
    def is_displayed(player: Player):
        return player.sex == 4


page_sequence = [SexAgeSurvey, SexOther]
