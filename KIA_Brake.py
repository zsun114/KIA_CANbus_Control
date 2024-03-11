import can
import cantools
import time
from inputs import get_gamepad
from pprint import pprint
db = cantools.database.load_file('directory of dbc file')#need to chage your own directory where you put dbc file
# Initialize the CANbus port
bus = can.interface.Bus(channel = 'can0', bustype= 'socketcan_native')

# the ID of CAN mesage through the Braking function

BRAKE_ID = None
for message in bus:
    if message.arbitration_id == 881:  ##Braking Pedal position message ID
        BRAKE_ID = message.arbitration_id
        break

# Reading Braking Pedal message
def read_beake_data()
    time_start = time.time()
    try:
        while True:
            message = bus.recv()
            if message is not None:
                try:
                    #Decoding CAN message
                    message_decoded = db.decode_message(message.arbitration_id, message.data)
                    if message.arbitration_id == BRAKE_ID
                        brake_message = message.data[0] 
                        pprint("Brake message:", brake_message)
                        time_duration = time.time() - time_start
                        dataList.append({'Duration': time_duration, 'data': brake_message})
                except Exception as e:
                    a = 0
    except:
        pass


def update_brake_pressure():
    global brake_pressure
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Absolute" and event.code == "ABS_Z"
                brake_pressure = int(event.state / 2.55) 
                brake_message = can.Message(arbitration_id=BRAKE_ID, data=[brake_pressure])
                # 发送刹车控制消息
                try:
                    bus.send(brake_message)
                    print("Brake control message sent successfully. Brake pressure:", brake_pressure)
                except can.CanError:
                    print("Error sending brake control message.")
    time.sleep(0.01)

# 启动键盘输入捕获线程
import threading
joystick_thread = threading.Thread(target=update_brake_pressure)
joystick_thread.daemon = True
joystick_thread.start()

# Sending message
while True:
    time.sleep(0.1)