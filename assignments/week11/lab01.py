"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperature():
    box = [1,2,3,4,5,6,7]
    #i=0
    #while i <= 6:
        #temp = int(input("enter the temperature : "))
        #box.append(temp)
        #i+=1
    return box

def analyze_temp(box):
    maxTemp = max(box)
    minTemp = min(box)
    avgTemp = sum(box)/len(box)
    return avgTemp,maxTemp,minTemp
    pass

def display_Analysis(avgTemp,maxTemp,minTemp):
    print(f"Temperature Analysis for the Week:\nAverage {avgTemp} C\nHighest: {maxTemp} C\nLowest: {minTemp} C")
    pass

box = get_temperature()
avgt,maxt,mint = analyze_temp(box)
display_Analysis(avgt,maxt,mint)