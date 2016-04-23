#!/usr/bin/python

from HTMLParser import HTMLParser
from Stack import Stack
from MenuStateMachine import MenuStateMachine
from StateMachineHandler import StateMachineHandler

class MenuParser(HTMLParser):
    _openTags = Stack()
    _stateMachine = MenuStateMachine()
    
    def get_open_tag(self):
        return self._openTags.top()
    
    def handle_starttag(self, tag, attrs):
        #print tag, StateMachineHandler.get_current_lookup_tag(self._stateMachine.get_current_state())
        if StateMachineHandler.match_open_tag(tag, self._stateMachine.get_current_state()):
            self._openTags.push(tag)
            state = self._stateMachine.get_current_state()
            if  state > MenuStateMachine.STATE_TITLES_TABLE and state < MenuStateMachine.STATE_DONE:
                print "-------------------------%s-------------------------" % StateMachineHandler.to_string(state)
            self._stateMachine.go_to_next_state()

    def handle_endtag(self, tag):
        self._openTags.pop()

    def handle_data(self, data):
        state = self._stateMachine.get_current_state()
        if state > MenuStateMachine.STATE_TITLES_TABLE+1 and state < MenuStateMachine.STATE_DONE+1:
            data = data.strip()
            if data and not data.isspace():
                print data
        

def testMenuParser():
    parser = MenuParser()
    parser.feed('<html><p class="titulo"> Cardapio dos Restaurantes - 25/04/2016 (segunda-feira)</p><table><span class="titulo_cardapio">Cafe da manha</span></table></html>')
    
#testMenuParser()




