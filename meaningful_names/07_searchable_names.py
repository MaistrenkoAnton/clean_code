s = 0
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for j in range(34):
    s += (t[j]*4) / 5

real_days_per_ideal_day = 4
work_day_per_week = 5
sum = 0
task_estimate = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for j in range(34):
    real_task_days = task_estimate[j] * real_days_per_ideal_day
    real_task_weeks = real_task_days / work_day_per_week
    sum += real_task_weeks
