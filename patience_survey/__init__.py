from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'patience_survey'
    players_per_group = None
    num_rounds = 1
    values = {
        'v100': 100,
        'v103': 103,
        'v106': 106,
        'v109': 109,
        'v112': 112,
        'v116': 116,
        'v119': 119,
        'v122': 122,
        'v125': 125,
        'v129': 129,
        'v132': 132,
        'v136': 136,
        'v139': 139,
        'v143': 143,
        'v146': 146,
        'v150': 150,
        'v154': 154,
        'v158': 158,
        'v161': 161,
        'v165': 165,
        'v169': 169,
        'v173': 173,
        'v177': 177,
        'v181': 181,
        'v185': 185,
        'v189': 189,
        'v193': 193,
        'v197': 197,
        'v202': 202,
        'v206': 206,
        'v210': 210,
        'v215': 215,
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    displayed_value = models.IntegerField()
    choice1patience = models.BooleanField()
    choice2patience = models.BooleanField()
    choice3patience = models.BooleanField()
    choice4patience = models.BooleanField()
    choice5patience = models.BooleanField()
    patience = models.IntegerField()
    willingness_to_act = models.IntegerField(
        label='How willing are you to give up something that is beneficial for you today in order to benefit more from '
              'that in the future? Please indicate your answer on a scale from 0 to 10, where 0 means you are '
              '“completely unwilling to do so” and 10 means you are “very willing to do so”. You can also use any '
              'numbers between 0 and 10 to indicate where you fall on the scale.',
        choices=[
            [0, '0'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10']
        ],
        widget=widgets.RadioSelectHorizontal
    )


# PAGES
class InstructionStaircase(Page):
    pass


class Choice1(Page):
    pass

    form_model = 'player'
    form_fields = ['choice1patience']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = player.choice1patience
        if choices == 1:
            player.participant.vars['key'] = Constants.values['v185']
        else:
            player.participant.vars['key'] = Constants.values['v125']


class Choice2(Page):
    pass

    form_model = 'player'
    form_fields = ['choice2patience']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            displayed_value=player.participant.vars['key']
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = (player.choice1patience, player.choice2patience)
        if choices == (1, 1):
            player.participant.vars['key'] = Constants.values['v202']
        elif choices == (1, 0):
            player.participant.vars['key'] = Constants.values['v169']
        elif choices == (0, 1):
            player.participant.vars['key'] = Constants.values['v139']
        else:  # choices == (0, 0)
            player.participant.vars['key'] = Constants.values['v112']


class Choice3(Page):
    pass

    form_model = 'player'
    form_fields = ['choice3patience']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            displayed_value=player.participant.vars['key']
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = (player.choice1patience, player.choice2patience, player.choice3patience)
        if choices == (1, 1, 1):
            player.participant.vars['key'] = Constants.values['v210']
        elif choices == (1, 1, 0):
            player.participant.vars['key'] = Constants.values['v193']
        elif choices == (1, 0, 1):
            player.participant.vars['key'] = Constants.values['v177']
        elif choices == (1, 0, 0):
            player.participant.vars['key'] = Constants.values['v161']
        elif choices == (0, 1, 1):
            player.participant.vars['key'] = Constants.values['v146']
        elif choices == (0, 1, 0):
            player.participant.vars['key'] = Constants.values['v132']
        elif choices == (0, 0, 1):
            player.participant.vars['key'] = Constants.values['v119']
        else:  # choices == (0, 0, 0)
            player.participant.vars['key'] = Constants.values['v106']


class Choice4(Page):
    pass

    form_model = 'player'
    form_fields = ['choice4patience']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            displayed_value=player.participant.vars['key']
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = (player.choice1patience, player.choice2patience, player.choice3patience, player.choice4patience)
        if choices == (1, 1, 1, 1):
            player.participant.vars['key'] = Constants.values['v215']
        elif choices == (1, 1, 1, 0):
            player.participant.vars['key'] = Constants.values['v206']
        elif choices == (1, 1, 0, 1):
            player.participant.vars['key'] = Constants.values['v197']
        elif choices == (1, 1, 0, 0):
            player.participant.vars['key'] = Constants.values['v189']
        elif choices == (1, 0, 1, 1):
            player.participant.vars['key'] = Constants.values['v181']
        elif choices == (1, 0, 1, 0):
            player.participant.vars['key'] = Constants.values['v173']
        elif choices == (1, 0, 0, 1):
            player.participant.vars['key'] = Constants.values['v165']
        elif choices == (1, 0, 0, 0):
            player.participant.vars['key'] = Constants.values['v158']
        elif choices == (0, 1, 1, 1):
            player.participant.vars['key'] = Constants.values['v150']
        elif choices == (0, 1, 1, 0):
            player.participant.vars['key'] = Constants.values['v143']
        elif choices == (0, 1, 0, 1):
            player.participant.vars['key'] = Constants.values['v136']
        elif choices == (0, 1, 0, 0):
            player.participant.vars['key'] = Constants.values['v129']
        elif choices == (0, 0, 1, 1):
            player.participant.vars['key'] = Constants.values['v122']
        elif choices == (0, 0, 1, 0):
            player.participant.vars['key'] = Constants.values['v116']
        elif choices == (0, 0, 0, 1):
            player.participant.vars['key'] = Constants.values['v109']
        else:  # choices == (0, 0, 0, 0)
            player.participant.vars['key'] = Constants.values['v103']


class Choice5(Page):
    pass

    form_model = 'player'
    form_fields = ['choice5patience']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            displayed_value=player.participant.vars['key']
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choices = (player.choice1patience, player.choice2patience, player.choice3patience, player.choice4patience,
                   player.choice5patience)
        if choices == (1, 1, 1, 1, 1):
            player.patience = 1
        elif choices == (1, 1, 1, 1, 0):
            player.patience = 2
        elif choices == (1, 1, 1, 0, 1):
            player.patience = 3
        elif choices == (1, 1, 1, 0, 0):
            player.patience = 4
        elif choices == (1, 1, 0, 1, 1):
            player.patience = 5
        elif choices == (1, 1, 0, 1, 0):
            player.patience = 6
        elif choices == (1, 1, 0, 0, 1):
            player.patience = 7
        elif choices == (1, 1, 0, 0, 0):
            player.patience = 8
        elif choices == (1, 0, 1, 1, 1):
            player.patience = 9
        elif choices == (1, 0, 1, 1, 0):
            player.patience = 10
        elif choices == (1, 0, 1, 0, 1):
            player.patience = 11
        elif choices == (1, 0, 1, 0, 0):
            player.patience = 12
        elif choices == (1, 0, 0, 1, 1):
            player.patience = 13
        elif choices == (1, 0, 0, 1, 0):
            player.patience = 14
        elif choices == (1, 0, 0, 0, 1):
            player.patience = 15
        elif choices == (1, 0, 0, 0, 0):
            player.patience = 16
        elif choices == (0, 1, 1, 1, 1):
            player.patience = 17
        elif choices == (0, 1, 1, 1, 0):
            player.patience = 18
        elif choices == (0, 1, 1, 0, 1):
            player.patience = 19
        elif choices == (0, 1, 1, 0, 0):
            player.patience = 20
        elif choices == (0, 1, 0, 1, 1):
            player.patience = 21
        elif choices == (0, 1, 0, 1, 0):
            player.patience = 22
        elif choices == (0, 1, 0, 0, 1):
            player.patience = 23
        elif choices == (0, 1, 0, 0, 0):
            player.patience = 24
        elif choices == (0, 0, 1, 1, 1):
            player.patience = 25
        elif choices == (0, 0, 1, 1, 0):
            player.patience = 26
        elif choices == (0, 0, 1, 0, 1):
            player.patience = 27
        elif choices == (0, 0, 1, 0, 0):
            player.patience = 28
        elif choices == (0, 0, 0, 1, 1):
            player.patience = 29
        elif choices == (0, 0, 0, 1, 0):
            player.patience = 30
        elif choices == (0, 0, 0, 0, 1):
            player.patience = 31
        elif choices == (0, 0, 0, 0, 0):
            player.patience = 32


class InstructionWillingnessToAct(Page):
    pass

    form_model = 'player'
    form_fields = ['willingness_to_act']


page_sequence = [InstructionStaircase, Choice1, Choice2, Choice3, Choice4, Choice5, InstructionWillingnessToAct]
