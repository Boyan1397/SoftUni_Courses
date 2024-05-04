days = int(input())
plunder_per_day = int(input())
target_plunder = float(input())
final_plunder = 0
for day in range(1,days+1):
    final_plunder += plunder_per_day
    if day % 3 == 0:
        final_plunder += (plunder_per_day / 2)
    if day % 5 == 0:
        fifth_day = final_plunder * 0.3
        final_plunder -= fifth_day
if final_plunder >= target_plunder:
    print(f"Ahoy! {final_plunder:.2f} plunder gained.")
elif final_plunder < target_plunder:
    percentage = (final_plunder / target_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")