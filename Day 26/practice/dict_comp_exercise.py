# Dictionary Comprehension practice #1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# Dictionary Comprehension practice #2
# Convert weather_c to weather_f dictionary
def f(temp):
    return temp * 9/5 + 32

weather_c = { 
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}


weather_f = {day: f(temp) for day, temp in weather_c.items()}
print(weather_f)