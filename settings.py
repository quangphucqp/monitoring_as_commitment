from os import environ
# Adjust Tetris parameters in js file

SESSION_CONFIGS = [
    dict(
        name='version_check',
        app_sequence=['_code_version'],
        num_demo_participants=1,
    ),
    dict(
        name='full_control_sequence',
        app_sequence=['instruction', 'minimum_work_week1', 'allocation', 'thanks_week1',
                      'welcome_week2', 'minimum_work_week2', 'additional_work_intro_week2', 'additional_work_week2',
                      'welcome_week3', 'minimum_work_week3', 'additional_work_week3',
                      'survey_intro_week3', 'patience_survey', 'perceived_bias_survey', 'wtp_control_survey',
                      'sex_age_survey', 'end'],
        num_demo_participants=1,
    ),
    dict(
        name='full_monitored_sequence',
        app_sequence=['instruction', 'minimum_work_week1', 'allocation', 'mon_instruction', 'thanks_week1',
                      'welcome_week2', 'minimum_work_week2', 'additional_work_intro_week2', 'additional_work_week2',
                      'welcome_week3', 'minimum_work_week3', 'additional_work_week3',
                      'survey_intro_week3', 'patience_survey', 'perceived_bias_survey', 'wtp_monitored_survey',
                      'sex_age_survey', 'end'],
        num_demo_participants=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
DEBUG = False

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4797708565631'

