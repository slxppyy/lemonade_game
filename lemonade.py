import random as rand

weather_list = ["hot", "cold", "rainy", "snowy", "cloudy"]
weather = rand.choice(weather_list)
print("Welcome to the lemonade game!")
print("Day 1: ")
print("Weather: {}".format(weather))