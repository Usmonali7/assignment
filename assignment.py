
def classify(value):
    if value < 118:
        return "Below range"
    elif value <= 122:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result


number_of_candles = int(input("Enter the number of candles: "))

total_height = 0
below_count = 0
in_range_count = 0
above_count = 0

for i in range(number_of_candles):
    height = int(input("Enter the candle height: "))

    classification = classify(height)
    print(classification)

    total_height += height

    if classification == "Below range":
        below_count += 1
    elif classification == "In range":
        in_range_count += 1
    else:
        above_count += 1

average_height = calculate_average(total_height, number_of_candles)

print(f"Total height: {total_height} mm")
print(f"Average height: {average_height} mm")
print(f"Below range: {below_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_count}")
