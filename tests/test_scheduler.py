from backend.scheduler import generate_timetable

def test_timetable():
    data = {
        "subjects": ["Math", "Physics"],
        "slots": ["Mon 9AM", "Mon 10AM"]
    }
    result = generate_timetable(data)
    assert "timetable" in result