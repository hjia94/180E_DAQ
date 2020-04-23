from scipy.optimize import fsolve
import math


probe_in = 30.0
probe_out_initial = 34.0

def calculate_motor(x,y,z):
    x+=probe_in
    D = math.sqrt(x**2 + y**2 + z**2)
    motor_y = probe_out_initial * y / x
    probe_out = math.sqrt(probe_out_initial**2 + motor_y**2)
    motor_z = probe_out * z / D
    motor_y = motor_y - y * 0.06 * (0.015 * motor_z**2 + 0.1 * abs(motor_z))
    motor_x = D - probe_in
    return motor_x, motor_y, motor_z


motor_x, motor_y, motor_z = calculate_motor(1.0, 1.0, 1.0)
print(motor_x, motor_y, motor_z)

# motor_x =
# motor_y =
# motor_z =

a = probe_in
b = probe_out_initial
xm = motor_x + probe_in
ym = motor_y
zm = motor_z
c = 0.06 * (0.015 * zm**2 + 0.1 * abs(zm))

def equations(v):
    x = v
    f1 = xm**2 - x**2 - ym**2 / (b / x - c)**2 - (zm * xm / b)**2 / (1 + (ym / (b - c * x)**2)
    #xm, ym, zm = 1
    # f1 = math.sqrt(xp**2 + yp**2 + zp**2)-1
    # f2 = b * yp / xp + s - 1
    # f3 = -1 + zp * b * (1 + yp**2 / xp**2) / math.sqrt(xp**2 + yp**2 + zp**2)
    # f1 = (a - (e/a) * (x**2)) * be**2 * e - c**2
    # f2 = z - math.sqrt(a**2 - e * (x**2))
    # f3 = y - d*x
    return (f1)

x = fsolve(equations, -5)
x = x[0]
z = math.sqrt(xm**2 - x**2 - ym**2 / (b / x - c)**2)
y = ym / (b / x - c)
# z = math.sqrt(a**2 - e * (x**2))
# y = d*x
print(type(x),type(y),type(z))
print(x, y, z)
