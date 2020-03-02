import krpc
from pid import PIDController

throttle_controller = PIDController(0.5, 0.2, 0.5)
goal_speed = 120

conn = krpc.connect(name='Hello World')
vessel = conn.space_center.active_vessel
control = vessel.control
ref_frame = vessel.orbit.body.reference_frame
flight = vessel.flight(ref_frame)
while True:
    output_throttle = throttle_controller.trigger(goal_speed, flight.speed, 1)
    control.throttle = output_throttle

    if output_throttle < -0.1:
        control.brakes = True
    else:
        control.brakes = False
    print("Speed: {}, Throttle: {}".format(flight.speed, output_throttle))
