
from tracker import core
import os

def test_add_and_mark():
    core.add_habit("Test Habit")
    core.mark_done("Test Habit")
    core.list_habits()
