# Arrangement module allows you to control FL Studio Playlist Arrangements

def jumpToMarker(index, select):
    """ Select a marker.
    
    index -- Set to -1, to select the previous marker or to +1 to select the next marker.
    
    select -- Set to true to select marker as well. """

def getMarkerName(index):
    """ Returns the name of the requested marker.
    If the marker doesn't exist, an empty string is returned. """

def addAutoTimeMarker(time, name):
    """ Add an automatic time marker at "time" with its name set to "name". """

def liveSelection(time, stop):
    """ Set a live selection point at "time".
    
    stop -- Set to true, to use end point of the selection (instead of start). """

def liveSelectionStart():
    """ Returns the start time of the current live selection. """

def currentTime(snap):
    """ Returns the current time in the current arrangement.
    
    snap -- Set to true, to get returned value snapped to the grid. """

def currentTimeHint(mode, time, setRecPPB=0, isLength=0):
    """ Returns a hint string for the requested "time" in the current arrangement.
    
    mode -- is 0 for pattern mode and 1 for song mode. """

def selectionStart():
    """ Returns the start time of the current selection in the current arrangement. """

def selectionEnd():
    """ Returns the end time of the current selection in the current arrangement. """