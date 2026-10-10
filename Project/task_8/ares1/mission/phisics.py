import math

G0 = 9.80665

def delta_v(m0, m1, isp=300):
    """Формула Циолковского, м/с."""
    if m1 <= 0 or m0 < m1:
        raise ValueError("Требуется m0 >= m1 > 0")
    return isp * G0 * math.log(m0 / m1)

def flight_time(distance_km, accel):
    """Время перелёта в часах: разгон на полпути + торможение."""
    return (2 * math.sqrt(((distance_km*1000) / 2) / accel)) / 3600

def fuel_needed(m_dry, target_dv, isp=300):
    """Масса топлива для заданного dv (обратная формула Циолковского)."""
    return m_dry * (math.exp(target_dv / (isp * G0)) - 1)
