from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_intro_week3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class SurveyIntro(Page):
    pass


page_sequence = [SurveyIntro]
