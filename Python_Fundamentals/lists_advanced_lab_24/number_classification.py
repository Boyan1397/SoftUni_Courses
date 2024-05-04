numbers = [int(s) for s in input().split(", ")]

positives_list = [str(p) for p in numbers if p >= 0]
negatives_list = [str(n) for n in numbers if n < 0]
evens_list = [str(ev) for ev in numbers if ev % 2 == 0]
odds_list = [str(od) for od in numbers if od % 2 != 0]

print(f"Positive: {', '.join(positives_list)}")
print(f"Negative: {', '.join(negatives_list)}")
print(f"Even: {', '.join(evens_list)}")
print(f"Odd: {', '.join(odds_list)}")
