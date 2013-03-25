from psychopy import microphone
from psychopy import event, visual  # for key events

microphone.switchOn(sampleRate=16000)  # do once

# Record for 1.000 seconds, save to mic.savedFile
mic = microphone.AudioCapture()
mic.record(1)
mic.playback()

# Resample, creates a new file discards orig
mic.resample(48000, keep=False)

# Record new file for 60 sec or until key 'q'
w = visual.Window()  # needed for key-events
mic.reset()
mic.record(60, block=False)
while mic.recorder.running:
    if 'q' in event.getKeys():
        mic.stop()