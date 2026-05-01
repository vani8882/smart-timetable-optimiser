def generate_timetable(data):
    subjects = data.get("subjects", [])
    slots = data.get("slots", ["Mon 9AM", "Mon 10AM", "Tue 9AM"])

    timetable = {}
    for i, subject in enumerate(subjects):
        timetable[subject] = slots[i % len(slots)]

    return {
        "timetable": timetable,
        "conflicts": 0
    }