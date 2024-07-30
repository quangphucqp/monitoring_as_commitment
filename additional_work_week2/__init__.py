from otree.api import *
from datetime import datetime
import pytz
import time
from parameters import Params
from notification import Noti

doc = """
Additional Work Week 2
Logic:
- Set num_rounds to 50
- Will repeat at most 50 times
- Players can enter Pause screen
- Can return to work from Pause screen
- End-of-day / run out of Additional Work: show EndPage
- Send notification if 1) complete fewer than planned AND 2) decide to pause
- "allocation_week2/3" DO NOT affect length of app: they are purely informational values.
"""


class Constants(BaseConstants):
    name_in_url = 'additional_work_week2'
    players_per_group = None
    num_rounds = Params.additional_work_week2_max_tasks  # Maximum number of rounds: 50

    # Set ending time, to carry over balances to Week 3
    local_tz = pytz.timezone('Europe/Amsterdam')  # This is the timezone for Amsterdam
    end_date_naive = datetime.strptime(Params.end_date_naive_week2, '%Y-%m-%d %H:%M')
    end_date_local = local_tz.localize(end_date_naive)
    end_date = end_date_local
    end_time = end_date.timestamp()  # Use this for timeout condition


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    complete = models.BooleanField(initial=False)
    remaining = models.IntegerField()
    pause = models.BooleanField(initial=False)  # Allow user to pause
    pause_this_round = models.BooleanField(initial=False)  # Keep track of pausing history
    pause_at_time = models.FloatField()  # Time at which player paused
    # Control timing at pause:
    time_till_session_ends = models.FloatField()  # Time at which player can progress to EndPage
    can_continue_at_time = models.FloatField()  # (Obsolete) Time at which player can continue

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

    @staticmethod
    def is_displayed(player: Player):
        return player.pause == 0

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
        player.remaining = Constants.num_rounds - player.round_number
        player.participant.vars['task_remaining'] = Constants.num_rounds - player.round_number


class ResultCanPause(Page):
    pass

    form_model = 'player'
    form_fields = ['pause']

    @staticmethod
    def is_displayed(player: Player):
        return player.pause == 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            tasks_completed=player.round_number
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # If pause then pause_this_round = True, but not otherwise
        player.pause_this_round = player.pause

        # If pause:
        if player.pause == 1:
            # Record time at which player paused
            player.pause_at_time = time.time()
            # Calculate time at which Week 2 automatically ends
            player.time_till_session_ends = Constants.end_time - player.pause_at_time

            # (Obsolete) Calculate time at which player can continue
            player.can_continue_at_time = player.pause_at_time + Params.rest_time

            # Keep track of how many times paused
            player.participant.vars['pause_counter_week2'] += 1
            # Send notification to Telegram if not yet reached limit
            if player.round_number < player.participant.vars['allocation_week2'] \
                    and player.participant.vars['pause_counter_week2'] <= Params.notification_limit:
                Noti.send_telegram_message(player.participant.vars['personal_code'])


class Pause(Page):
    pass

    form_model = 'player'
    form_fields = ['pause']

    @staticmethod
    def is_displayed(player: Player):
        return player.pause == 1

    @staticmethod
    # Don't forget to toggle the CSS in Pause.html to show/hide the timer
    def get_timeout_seconds(player: Player):
        return max(player.time_till_session_ends, 0.01)  # return timeout_happened if time is up

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            tasks_completed=player.round_number
        )

    @staticmethod
    def app_after_this_page(player: Player, timeout_happened):
        if timeout_happened:  # Send to EndPage if time is up (player not return to work)
            player.pause = 0
            return 'welcome_week3'

        # Call Noti.send_telegram_message if player has not reached limit of tasks
        if player.pause == 0 and player.round_number < player.participant.vars['allocation_week2'] \
                and player.participant.vars['pause_counter_week2'] <= Params.notification_limit:
            message = player.participant.vars['personal_code'] + " continued"
            Noti.send_telegram_message(message)


'''
class PauseWaitPage(Page):
    pass

    # Set timeout to rest_time so that players are automatically advanced if they do not refresh
    @staticmethod
    def get_timeout_seconds(player: Player):
        return max( player.can_continue_at_time - time.time(), 0.01)  # Ensure that the real wait time is the rest_time

    @staticmethod
    def is_displayed(player: Player):
        return player.pause == 1 and time.time() < player.can_continue_at_time

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            tasks_completed=player.round_number
        )
'''


class EndPage(Page):
    pass

    timeout_seconds = 10

    @staticmethod  # Same time condition as LandingPage2, but different app
    def is_displayed(player: Player):
        return player.remaining == 0 or time.time() > Constants.end_date.timestamp()

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return 'welcome_week3'


page_sequence = [TetrisPage, ResultCanPause, Pause, EndPage]
