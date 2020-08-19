import pytest

@pytest.mark.usefixtures("clean_room_mission_manager")
def test_clean_room_mission_manager(clean_room_mission_manager):
    plan = clean_room_mission_manager.plan()
    assert plan is None
