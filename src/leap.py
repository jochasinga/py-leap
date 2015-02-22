import sys
sys.path.insert(0, "../lib")

import gevent
import Leap

def on_connect(controller):
    if controller.is_connected:
        print "Connected"
    
def on_frame(controller):
    while True:
        frame = controller.frame()
        if frame.is_valid:
            frame = controller.frame()
            print "timestamp: %d | hands: %d | fingers: %d" % (
                frame.timestamp, len(frame.hands), len(frame.fingers),
            )

def on_kill():
    # Keep this process running until interrupted
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        gevent.kill()


def main():

    # Create a controller 
    ctrlr = Leap.Controller()

    # Start the coroutines
    gevent.joinall([
        gevent.spawn(on_connect, ctrlr),
        gevent.spawn(on_frame, ctrlr),
        gevent.spawn(on_kill)
    ])
    
if __name__ == "__main__":
    main()

    
