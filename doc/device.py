
def isAssigned():
    """ Send a SYSEX message to the (linked) output interface. """

def getPortNumber():
    """ Returns the interface port number (or -1 when port number is not assigned).
    This is same number as the interface port number set in FL Studio MIDI settings. """

def midiOutMsg(message):
    """ Send a MIDI message to the (linked) output interface.
    
    message -- holds the value to be sent, with the channel and command in the lower byte and the first and second data values in the next two bytes. 
    
    """

def midiOutNewMsg(slotIndex, message):
    """ Send a MIDI message to the (linked) output interface, but only if the value has changed.
    
    slotIndex -- value chosen by the caller, it should be the same as it was for the previous message that should be compared with.
    
    message -- holds the value to be sent. """

def midiOutSysex(message):
    """ Send a SYSEX message to the (linked) output interface. """

def sendMsgGeneric(id, message, lastMsg, offset=0):
    """ Send a text string as a SYSEX message to the (linked) output interface.
    
    id -- holds the first 6 bytes of the message (starting with 0xF0). The end value 0xF7 is added automatically.
    
    message -- is the text to send.
    
    lastMsg -- is the string returned by the previous call to this function.
    function returns updated lastMsg. """

def processMIDICC(eventData):
    """ Let FL process a CC message.
    Use this function inside OnMidiMsg and pass (modified) eventData object as function parameter. """

def directFeedback(eventData):
    """ Send a received message on to the (linked) output device.
    Use this function inside OnMidiMsg and pass (modified) eventData object as function parameter """

def repeatMidiEvent(eventData, delay=300, rate=300):
    """ Start repeatedly sending out the previously sent message.
    It will be sent first after "delay" milliseconds, and afterwards every "rate" milliseconds. """

def stopRepeatMidiEvent():
    """ Stop repeating the message sent with repeatMidiEvent. """

# Control events

def findEventID(controlId, flags=[]):
    """ Returns eventID for controlId.
    
    flags -- can be one of the following: FEID_Flags_Skip_Unsafe = 1 (skip unsafe (using formula) links) """

def getLinkedValue(eventID):
    """ Returns eventID for controlId.
    
    flags -- can be one of the following: FEID_Flags_Skip_Unsafe = 1 (skip unsafe (using formula) links) """

def getLinkedInfo(eventID):
    """ Returns information about the linked control via eventID
    (to get control eventId, use findEventID function).
    Result is -1 if there is no linked control, otherwise result is one or more of the constants. """

# Refresh thread

def createRefreshThread():
    """ Start a threaded refresh of the entire MIDI device. """

def destroyRefreshThread():
    """ Stop a previously started threaded refresh. """

def fullRefresh():
    """ Trigger a previously started threaded refresh.
    If there is none, the refresh is triggered immediately. """

# Helpers

def isDoubleClick(long_index):
    """ Returns True if the function was called with the same index shortly before, indicating a double click. """

def setHasMeters():
    """ use this in OnInit event to tell FL Studio device use peak meters """

def baseTrackSelect(index, step):
    """ Base track selection (for control surfaces). Set step to MaxInt for reset. """

def hardwareRefreshMixerTrack(index):
    """ Hardware refresh mixer track at "index", use -1 to refresh all """
