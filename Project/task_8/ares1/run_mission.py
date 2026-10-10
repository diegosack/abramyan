"""Запуск: python run_mission.py --days 6 --seed 42"""
import argparse, sched, time
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    p.add_argument("--days",  type=int,   default=5,   help="длительность миссии, сут")
    p.add_argument("--seed",  type=int,   default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.2, help="секунд на 1 сутки")
    return p

def main():
    args = build_parser().parse_args()
    resource = 100
    s = sched.scheduler(time.time, time.sleep)
    m_dry = 45000
    m_start = 97000
    target_dv = 6700
    distance_km = 23455556
    accel = 0.0045
    print("==============================================================")
    print(" МИССИЯ «АРЕС-1»: Марс")
    print("==============================================================")
    
    dv_calculated = delta_v(m_start, m_dry)
    fuel_calc = fuel_needed(m_dry, target_dv)
    time_calc = flight_time(distance_km, accel)
        
    print(f"Характеристическая скорость (Циолковский): {dv_calculated:.1f} м/с")
    print(f"Топлива для dv = {target_dv} м/с при сухой массе 20 т: {fuel_calc:,.0f} кг".replace(",", " "))
    print(f"Время перелёта {distance_km/1000000:.3f} тыс. км при a = {accel} м/с^2: {time_calc:,.0f} ч = {time_calc/24:.0f} сут".replace(",", " "))
    print("--------------------------------------------------------------")
        
    def day_report(day):
        """Отчёт за сутки; при исчерпании ресурса отменяет все задачи."""
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        print(f"Сутки {day:>2} | {desc:<38s} {delta:+3d} | ресурс {resource:3d}% "
              f"{'#' * (resource // 5)}")
        if resource == 0:
            for ev in list(s.queue):
                s.cancel(ev)
            return
        if day < args.days:
            s.enter(args.speed, 1, day_report, (day + 1,))

    st = time.time()
    s.enter(args.speed, 1, day_report, (1,))
    s.run()
    f= time.time()
        
    print("--------------------------------------------------------------")
    print(f"Миссия завершена. Итоговый ресурс: {resource}%. "
        f"Реальное время симуляции: {f - st} c")


if __name__ == "__main__":
    main()
