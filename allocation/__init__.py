from otree.api import *

doc = """
Planning
"""


class Constants(BaseConstants):
    name_in_url = 'planning'
    players_per_group = None
    num_rounds = 1
    num_additional_task = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    allocation_week2 = models.IntegerField(min=0, max=Constants.num_additional_task, step=1)
    allocation_week3 = models.IntegerField(min=0, max=Constants.num_additional_task, step=1)


# PAGES
class AllocationPage(Page):
    pass

    form_model = 'player'
    form_fields = ['allocation_week3']

    # Export allocation_week2 and allocation_week3 to be used in the next apps
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.allocation_week2 = Constants.num_additional_task - player.allocation_week3
        player.participant.vars['allocation_week2'] = player.allocation_week2
        player.participant.vars['allocation_week3'] = player.allocation_week3


class Result(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            a=player.allocation_week2,
            b=player.allocation_week3,
        )


page_sequence = [AllocationPage, Result]
