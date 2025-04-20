def generate_plan(total_reps, exercise):
    if total_reps < 10:
        return f"Let's aim for 3 sets of 12 {exercise}s with rest in between."
    elif total_reps < 20:
        return f"You're doing well! Target 4 sets of 15 {exercise}s."
    else:
        return f"Great job! Try 5 sets of 20 {exercise}s with advanced variations."