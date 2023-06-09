import paho.mqtt.client as mqtt
import random
import time
import json
# Define the room size
ROOM_WIDTH = 4.0
ROOM_HEIGHT = 4.0

# Define the initial position of the person
x = random.uniform(0, ROOM_WIDTH)
y = random.uniform(0, ROOM_HEIGHT)

# Define the movement step size
STEP_SIZE = 1

# Define the standard deviation of the measurement noise
MEASUREMENT_STD_DEV = 0.5

def move():
    global x
    global y
    # Generate random movement in x and y direction
    dx = random.uniform(-STEP_SIZE, STEP_SIZE)
    dy = random.uniform(-STEP_SIZE, STEP_SIZE)

    # Update position
    x_new = x + dx
    y_new = y + dy

    # Make sure position stays within room boundaries
    x_new = max(0, min(x_new, ROOM_WIDTH))
    y_new = max(0, min(y_new, ROOM_HEIGHT))

    # Update position with noise
    x_new += random.gauss(0, MEASUREMENT_STD_DEV)
    y_new += random.gauss(0, MEASUREMENT_STD_DEV)

    # Update current position

    x, y = x_new, y_new

    return (x, y)
# Define the MQTT broker IP address and port
broker_address = "192.168.185.12"
# broker_address = "broker.hivemq.com"

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address)

# coordinates = [(2.63, -3.09),(3.5, -2.95), (3.5, 0), (0.9, 0), (0.9, 0.1), (3.5, 0.1), (3.5, 3.315), (-0, 3.315), (0, 0), (-0.165, 0),(-0.165, 3.315),(-2.495, 3.315), (-2.495, 2.845),(-2.87, 2.845), (-2.87, 1.785), (-0.92, 1.785), (-0.92, 1.685), (-3.455, 1.685), (-3.455, -3.09), (1.78, -3.09)] # Peta
coordinates = [(2.63, -3.09),(3.5, -3.09), (3.5, 0), (0.9, 0), (0.9, 0.1), (3.5, 0.1), (3.5, 3.315), (-0, 3.315), (0, 0), (-0.165, 0),(-0.165, 3.315),(-2.495, 3.315), (-2.495, 2.845),(-2.87, 2.845), (-2.87, 1.785), (-0.92, 1.785), (-0.92, 1.685), (-3.455, 1.685), (-3.455, -3.09), (1.78, -3.09)] # Peta tanpa sisi miring



# coordinates = [(2.63, -3.09),(3.5, 0), (0,0),(-0.6,0),(-0.6, -3.2)] ##RUANG TAMU
# coordinates = [(3.5, -3.09),(3.5, 0), (0,0),(-0.6,0),(0, -3.09)] ##RUANG TAMU TSM

# coordinates = [(3.5, 0.1), (3.5, 3.315), (-0, 3.315),(0,0.1)] ##KAMAR TIDUR

# coordinates = [(-3.455, 1.685), (-3.455, -3.09), (0,1.685), (0,-3.09)]# Ruang Makan

# coordinates = [(-0.165, 3.315), (-2.495, 3.315), (-2.495, 2.845), (-2.87, 2.845),(-2.87, 1.785),(-0.165, 1.785)]# Toilet



# i = 3
# Run an infinite loop to publish random numbers
while True:

 
       for i, coord in enumerate(coordinates):
        x, y = coord
       
        data = {
            "x": x,
            "y": y
        }
        json_data = json.dumps(data)
        client.publish("xy1", json_data)
        print(f"Sent coordinate {i+1}: ({x}, {y})")
        time.sleep(2) 


    # # Generate a random number between 1-10
    # random_numberx,random_numbery = move()
    
    # # Publish the random number to the MQTT topic
    # # client.publish(mqtt_topic, random_numberx)
    # # client.publish("x", random_numberx)
    # # client.publish("y", random_numbery)
    # coordinates = {
    #     "x": random_numberx,
    #     "y": random_numbery
    # }
    # # Convert the dictionary to JSON
    # json_data = json.dumps(coordinates)
    # client.publish("xy", json_data)
    # print("Sent coordinates:", json_data)

    # # print(random_numberx)
    # # print(random_numbery)
    # # client.publish(mqtt_topic, random_numbery)

    
    # # Wait for a second before publishing the next random number
    # time.sleep(2) # x *= 2.5
        # y *= 2.5
