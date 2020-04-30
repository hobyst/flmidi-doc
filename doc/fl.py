# Matches the "Script events" section of the FL Studio reference API

def OnInit():
    """ Called when the script has been started. """

def OnDeInit():
    """ Called before the script will be stopped. """

def OnIdle():
    """ Called from time to time. Can be used to do some small tasks, mostly UI related. 
    For example: update activity meters. """

def OnMidiIn(eventData):
    """ Called first when a MIDI message is received. Set the event's handled property to true if you don't want further processing.
    
    Only raw data is included here: handled, timestamp, status, data1, data2, port, sysex, pmeflags
    
    Use this event for filtering, use OnMidiMsg event for actual processing... """

def OnMidiMsg(eventData):
    """ Called for all MIDI messages that were not handled by OnMidiIn. """

def OnMidiOutMsg(eventData):
    """ Called for short MIDI out messages.
    
    Event properties are limited to: handled, status, data1, data2, port, midiId, midiChan, midiChanEx """

def OnNoteOn(eventData):
    """ Called for note on messages that were not handled by OnMidiMsg. """

def OnNoteOff(eventData):
    """ Called for note off messages that were not handled by OnMidiMsg. """

def OnControlChange(eventData):
    """ Called for CC messages that were not handled by OnMidiMsg. """

def OnProgramChange(eventData):
    """ Called for program change messages that were not handled by OnMidiMsg. """

def OnPitchBend(eventData):
    """ Called for pitch bend messages that were not handled by OnMidiMsg. """

def OnKeyPressure(eventData):
    """ Called for key pressure messages that were not handled by OnMidiMsg. """

def OnChannelPressure(eventData):
    """ Called for channel pressure messages that were not handled by OnMidiMsg. """

def OnRefresh(long_flags):
    """ Called when something changed that the script might want to respond to. """

def OnDoFullRefresh():
    """ Same as OnRefresh, but everything should be updated. """

def OnUpdateBeatIndicator(long_value):
    """ Called when the beat indicator has changes.
    "value" has the new value. 
    
    (TODO: needs detailed explanation of "value") """

def OnDisplayZone():
    """ Called when playlist zone changed. """

def OnUpdateLiveMode(long_lastTrack):
    """ Called when something about performance mode has changed. """

def OnDirtyMixerTrack():
    """ Called when mixer tracks changed. """

def OnUpdateMeters():
    """ Called when peak meters need to be updated. """

def OnWaitingForInput():
    """ (TODO: needs explanation) """

def OnSendTempMsg():
    """ (TODO: needs explanation) """