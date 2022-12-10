"""
Assignment Title: IoT Using Raspberry Pi and Firebase and Android
Purpose         : To create an android app and send data to Firebase RealTime Database.
Language        : Implementation in Python with Raspberry Pi 4
Author          : Hemant Ramphul
Github          : https://github.com/hemantramphul/IoT-Using-Raspberry-Pi-and-Firebase-and-Android
Date            : 01 December 2022

Université des Mascareignes (UdM)
Faculty of Information and Communication Technology
Master Artificial Intelligence and Robotics
Official Website: https://udm.ac.mu
"""

import time  # Import the sleep library, which responsible to do the timing stuff.
import random as rand  # Import random library
import pyrebase  # Import database module.

# Firebase configuration
# Dictionary named config with several key-value pairs that configure the connection to the database.
config = {
    "apiKey": "_enter_your_api_key_here_",
    "authDomain": "iotdht11sensor.firebaseapp.com",
    "projectId": "iotdht11sensor",
    'databaseURL': 'https://iotdht11sensor-default-rtdb.firebaseio.com/',
    "storageBucket": "iotdht11sensor.appspot.com",
    "messagingSenderId": "658125581309",
    "appId": "1:658125581309:web:127027f2624c1c3439c794",
    "measurementId": "G-64BXKX08FT"
}

# Initialize the communication with the "firebase" servers using the previous config data.
firebase = pyrebase.initialize_app(config)
# Take an instance from the firebase database which is pointing to the root directory of your database.
database = firebase.database()

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 15


# Define a function to save data to Firebase real time database
def saveSensorDataToFirebase(temperature, humidity):
    # Prepare data to save
    data = {
        "Humidity": humidity,  # set humidity
        "Temperature": temperature  # set temperature
    }

    # Get a child to database
    database.child("DHT11SensorData").child("SensorData").push(data)


# Define a function that will post [Temperature] and [Humidity] on Thingspeak server every 15 Seconds
def start():
    # Generate a random temperature
    temperature = rand.randint(-10, 40)
    # Generate a random humidity
    humidity = rand.randint(0, 35)

    # Display generated data in the console
    print('Temperature = {0:0.1f}℃ Humidity = {1:0.1f}%'.format(temperature, humidity))
    # Sending data to Firebase RealTime Database
    saveSensorDataToFirebase(temperature, humidity)


if __name__ == '__main__':
    while True:
        # Start the main function
        start()
        # Delay
        time.sleep(DHT_READ_TIMEOUT)
