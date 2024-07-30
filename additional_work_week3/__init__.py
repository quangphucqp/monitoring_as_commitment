from otree.api import *
from parameters import Params
from notification import Noti
import time

doc = """
Additional Work Week 3
Logic:
- Repeats at most 50 times (via num_rounds)
- Ending condition depends on "player.remaining"
- Send notification if decide to pause
"""


class Constants(BaseConstants):
    name_in_url = 'additional_work_week3'
    players_per_group = None
    num_rounds = Params.additional_work_week3_max_tasks         # Maximum num_rounds: 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    complete = models.BooleanField(initial=False)
    remaining_week3 = models.IntegerField()
    pause = models.BooleanField(initial=False)  # Allow user to pause
    pause_this_round = models.BooleanField(initial=False)  # Keep track of pausing history

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

    @staticmethod  # Skip if all additional work is done in Week 2
    def is_displayed(player: Player):
        return player.participant.vars['task_remaining'] > 0 or player.pause == 0

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

        # Calculate remaining tasks
        player.current_round_complete()
        player.remaining_week3 = player.participant.vars['task_remaining'] - player.round_number

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.remaining_week3 == 0 or player.participant.vars['task_remaining'] == 0:
            return 'survey_intro_week3'
        else:
            return {}


class ResultCanPause(Page):
    pass

    form_model = 'player'
    form_fields = ['pause']

    @staticmethod  # Skip if all additional work is done in Week 2
    def is_displayed(player: Player):
        return player.participant.vars['task_remaining'] > 0 or player.pause == 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            page_remain_additional=player.remaining_week3
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # If pause then pause_this_round = True, but not otherwise
        player.pause_this_round = player.pause
        if player.pause == 1:
            # Keep track of how many times paused
            player.participant.vars['pause_counter_week3'] += 1
            # Send notification to Telegram if not yet reached limit
            # (in Week 3, don't track allocation, only track "pause")
            if player.participant.vars['pause_counter_week3'] <= Params.notification_limit:
                Noti.send_telegram_message(player.participant.vars['personal_code'])


class Pause(Page):
    pass

    form_model = 'player'
    form_fields = ['pause']

    @staticmethod
    def is_displayed(player: Player):
        return player.pause == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            page_remain_additional=player.remaining_week3
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.participant.vars['pause_counter_week3'] <= Params.notification_limit:
            message = player.participant.vars['personal_code'] + " continued"
            Noti.send_telegram_message(message)


page_sequence = [TetrisPage, ResultCanPause, Pause]
