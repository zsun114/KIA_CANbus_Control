import can
import cantools
from opendbc.can.packer import CANPacker
from openpilot.selfdrive.car.hyundai import hyundaican
from openpilot.selfdrive.car.hyundai.values import CAR
from inputs import get_gamepad
from panda import Panda
db = cantools.database.load_file('hyundai_kia_generic.dbc')#need to chage your own directory where you put dbc file
# Initialize the CANbus port
bus = can.interface.Bus(channel = 'can0', bustype= 'socketcan_native')

#Init panda
p = Panda()

# Set safety mode to allow everything
p.set_safety_mode(p.SAFETY_ALLOUTPUT)

def update_brake_pressure():
    global brake_pressure
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Absolute" and event.code == "ABS_Z":
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