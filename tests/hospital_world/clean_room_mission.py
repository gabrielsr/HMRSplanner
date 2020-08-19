import pytest

from gmrs.model.mission.mission import Mission
from gmrs.model.mission.goal import Goal
from gmrs.model.mission.task import Task

from gmrs.model.context.location import Location

from gmrs.model.context.robot import Robot

from gmrs.utils.mission_specification import set_refinement, set_location
from gmrs.planner.manager import Manager
from gmrs.model.mission.operator import OP


# scenario context 
room = Location('room')

context = {}


# tasks
class ts:
    # leaf tasks
    identify_out_of_place_objects = Task('Identify out of place objects')
    move_objects = Task('Move Objects')
    sweep_floor = Task('Sweep Floor')
    uv_light_sterilize = Task('UV-Light Sterilize')

    # composite tasks
    tidy_objects = Task('Tidy Objects')
    clean_room = Task('Clean Room')
    clean_and_tidy_room = Task('Clean and Tidy Room (location)')


# refinements
set_refinement(
    OP.SEQ,
    ts.clean_and_tidy_room,
    (ts.tidy_objects,
     ts.clean_and_tidy_room)
)

goal = Goal(ts.clean_and_tidy_room)
mission = Mission(goal)


# world
# locations
class ls:
    robots_room = Location('robots_room')


# means
r1 = Robot('r1')
set_location(r1, ls.robots_room)


mission_manager = Manager(mission, context, [r1])


@pytest.fixture
def clean_room_mission_manager():
    return mission_manager
