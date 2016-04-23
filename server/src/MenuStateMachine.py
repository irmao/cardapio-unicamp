#!/usr/bin/python

class MenuStateMachine:
    STATE_MENU_TITLE = 0
    STATE_TITLES_TABLE = 1
    STATE_LUNCH = 2
    STATE_VEG_LUNCH = 3
    STATE_DINNER = 4
    STATE_VEG_DINNER = 5
    STATE_DONE = 6

    _currentState = STATE_MENU_TITLE

    def __init__(self):
        self._currentState = MenuStateMachine.STATE_MENU_TITLE
    
    def get_current_state(self):
        return self._currentState
    
    def go_to_next_state(self):
        if self._currentState < MenuStateMachine.STATE_DONE:
            self._currentState += 1
    
def testMenuStateMachine():
    stateMachine = MenuStateMachine()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_MENU_TITLE
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_TITLES_TABLE
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_LUNCH
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_VEG_LUNCH
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_DINNER
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_VEG_DINNER
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_DONE
    stateMachine.go_to_next_state()
    assert stateMachine.get_current_state() == MenuStateMachine.STATE_DONE

            
#testMenuStateMachine()
