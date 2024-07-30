from otree.api import *
from datetime import datetime
from parameters import Params
import pytz

doc = """
Real Effort Task with Tetris Game
"""


# DATA
class Constants(BaseConstants):
    name_in_url = 'welcome_week3'
    players_per_group = None
    num_rounds = 1

    # Set timezone
    local_tz = pytz.timezone('Europe/Amsterdam')  # This is the timezone for Amsterdam

    # Set the start_date
    start_date_naive = datetime.strptime(Params.start_date_naive_week3, '%Y-%m-%d %H:%M')
    start_date_local = local_tz.localize(start_date_naive)
    start_date_utc = start_date_local.astimezone(pytz.utc)

    # Set the end_date
    end_date_naive = datetime.strptime(Params.end_date_naive_week3, '%Y-%m-%d %H:%M')
    end_date_local = local_tz.localize(end_date_naive)
    end_date_utc = end_date_local.astimezone(pytz.utc)

    # Set start/end date
    start_date = start_date_local
    end_date = end_date_local


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    # Time data for display purpose
    start_time = models.FloatField()
    start_time_readable = models.StringField()
    end_time = models.FloatField()
    end_time_readable = models.StringField()

    def set_time_data(self):
        self.start_time = Constants.start_date.timestamp()
        self.start_time_readable = Constants.start_date.strftime('%A, %B %d, %H:%M')
        self.end_time = Constants.end_date.timestamp()
        self.end_time_readable = Constants.end_date.strftime('%A, %B %d, %H:%M')

    # Check if the session can begin/has ended:
    # returns True if the current time is before the designated start time
    def session_not_started(self):
        import time
        return time.time() < self.start_time

    # returns True if the current time is after the designated end time
    def session_ended(self):
        import time
        return time.time() > self.end_time


# PAGES
class WelcomePage(Page):
    pass

    @staticmethod
    def is_displayed(player: Player):
        player.set_time_data()
        return not (player.session_not_started() or player.session_ended())


class Work(Page):
    pass

    @staticmethod
    def is_displayed(player: Player):
        player.set_time_data()
        return not (player.session_not_started() or player.session_ended())


class LandingPage1(Page):
    """
    Users end up here before Week starts.
    Skipped during session.
    """
    pass

    @staticmethod
    def is_displayed(player: Player):
        player.set_time_data()
        return player.session_not_started()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        return "Player somehow tried to proceed past a page with no next button"


class LandingPage2(Page):
    """
    Users end up here after Week ends.
    Skipped during session.
    """
    pass

    @staticmethod
    def is_displayed(player: Player):
        player.set_time_data()
        return player.session_ended()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        return "Player somehow tried to proceed past a page with no next button"


page_sequence = [LandingPage1, LandingPage2, WelcomePage, Work]
