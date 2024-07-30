from otree.api import *
from parameters import Params
import time

doc = """
Instruction
"""


class Constants(BaseConstants):
    name_in_url = 'instruction'
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

    # Computer Number
    computer_number = models.IntegerField(
        label='Before beginning, please enter the computer number you are using:',
        widget=widgets.TextInput(),
    )

    # Consent
    consent = models.CharField(
        choices=['I have read the above information and agree to participate in this research.',
                 'I do not want to participate in this research.'],
        widget=widgets.RadioSelect
    )

    # Personal Code
    personal_code = models.StringField(
        label='Please type in your Personal Code:',
        widget=widgets.TextInput(),
    )
    personal_code_retype = models.StringField(
        label='Please type in your Personal Code again:',
        widget=widgets.TextInput(),
    )

    # Quiz
    quiz_answer1 = models.IntegerField(
        label='1. How many weeks are you required to participate?',
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    quiz_answer2 = models.IntegerField(
        label='2. In which week are you asked to come to the lab to participate?',
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    quiz_answer3 = models.BooleanField(
        label='3. Will you have to complete minimum work of 10 tasks in each week?',
        choices=[[True, 'Yes'], [False, 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    quiz_answer4 = models.BooleanField(
        label='4. Will you have to complete all tasks of additional work in one single week?',
        choices=[[True, 'Yes'], [False, 'No']],
        widget=widgets.RadioSelectHorizontal
    )
    quiz_answer5 = models.BooleanField(
        label='5. Will you be able to leave the unfinished additional work in Week 2 to Week 3?',
        choices=[[True, 'Yes'], [False, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    # Record time spent on task
    task_start_time = models.FloatField()
    task_end_time = models.FloatField()
    task_duration = models.FloatField()


# PAGES

class ComputerNumber(Page):
    pass

    form_model = 'player'
    form_fields = ['computer_number']


class ConsentForm(Page):
    pass

    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            irb_number=Constants.irb_number
        )


class ConsentFormReject(Page):
    pass

    @staticmethod
    def is_displayed(player: Player):
        return player.consent == 'I do not want to participate in this research.'

    # Track if the participant is in treatment group
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['monitored'] = Constants.monitored


class PersonalCode(Page):
    pass

    form_model = 'player'
    form_fields = ['personal_code', 'personal_code_retype']

    @staticmethod
    def error_message(player: Player, values):
        if values['personal_code'] != values['personal_code_retype']:
            return 'The two codes you typed in do not match. Please try again.'

    @staticmethod  # Store "personal code" to be called in later apps
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['personal_code'] = player.personal_code
        player.participant.vars['pause_counter_week2'] = 0  # Needed for notification functionality
        player.participant.vars['pause_counter_week3'] = 0


class Practice(Page):
    pass


class TetrisPage(Page):
    pass

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


class Quiz(Page):
    pass

    form_model = 'player'
    form_fields = ['quiz_answer1', 'quiz_answer2', 'quiz_answer3', 'quiz_answer4', 'quiz_answer5']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz_answer1=3, quiz_answer2=1, quiz_answer3=True, quiz_answer4=False, quiz_answer5=True)

        if values != solutions:
            return 'One or more answers are incorrect. Please try again.'


class Work(Page):
    pass


page_sequence = [ComputerNumber, ConsentForm, ConsentFormReject, PersonalCode, Practice, TetrisPage, Quiz, Work]
