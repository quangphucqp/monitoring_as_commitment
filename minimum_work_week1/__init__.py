from otree.api import *
from parameters import Params
import time


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'minimum_work_week1'
    players_per_group = None
    num_rounds = Params.minimum_work_week1_tasks         # Week 1: set num_rounds = num_minimum_tasks
    num_minimum_tasks = Params.minimum_work_week1_tasks  # minimum number of tasks to complete


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    complete = models.BooleanField(initial=False)
    remaining = models.IntegerField()

    # Record time spent on task
    task_start_time = models.FloatField()
    task_end_time = models.FloatField()
    task_duration = models.FloatField()

    def current_round_complete(self):
        self.complete = True
        self.participant.vars['task_complete'] = True


# PAGES


class TetrisPage(Page):
    pass

    form_model = 'player'
    form_fields = []

    # When the page is loaded
    @staticmethod
    def vars_for_template(player: Player):
        player.task_start_time = time.time()
        return {}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        # Record time spent on task
        player.task_end_time = time.time()
        player.task_duration = player.task_end_time - player.task_start_time

        player.current_round_complete()
        player.remaining = Constants.num_minimum_tasks - player.round_number


class Result(Page):
    pass

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            page_remain=player.remaining
        )


page_sequence = [TetrisPage, Result]
