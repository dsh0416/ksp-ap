class PIDController:
    def __init__(self, kp, ki, kd, min_value=0.0, max_value=1.0):
        self.prev_err = 0
        self.integral = 0
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.min = min_value
        self.max = max_value
    
    def trigger(self, goal, measured, dt):
        err = goal - measured
        self.integral = self.integral + err * dt

        if self.integral < self.min:
            self.integral = self.min
        elif self.integral > self.max:
            self.integral = self.max

        derivative = (err - self.prev_err) / dt
        output = self.kp * err + self.ki * self.integral + self.kd * derivative
        self.prev_err = err
        return output
