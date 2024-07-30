# Parameters of strings / time used in the apps

class Params:

    # CODE VERSION
    code_version = '2023-10.25.Fri1103'

    # NUMBER OF TASKS
    minimum_work_week1_tasks = 10
    minimum_work_week2_tasks = 10
    minimum_work_week3_tasks = 10
    additional_work_week2_max_tasks = 50
    additional_work_week3_max_tasks = 50

    # Notification Limits: send notification to Telegram
    notification_limit = 0

    # Rest time (if implemented, still need to modify additional_work_week3)
    rest_time = 0 * 60  # in seconds

    # WEEK 1
    # Instruction App
    irb_number = 'IRB FUL 2023-003'

    # Monitor App
    monitor_phone = '+31 649 124409'
    day_in_week = 'Friday'

    # WEEK 2
    # Landing time
    start_date_naive_week2 = '2023-11-10 00:00'
    end_date_naive_week2 = '2023-11-10 23:59'

    # WEEK 3
    # Landing time
    start_date_naive_week3 = '2023-11-17 00:00'
    end_date_naive_week3 = '2023-11-17 23:59'

    # Restaurant name
    restaurant_name = 'KFC, Shinzo Sushi and Grill, De Burgerij, and Rodeo American Grill & Steak'
