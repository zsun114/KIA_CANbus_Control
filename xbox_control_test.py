import inputs
from inputs import get_gamepad

# 定义Xbox手柄按键代码
button_codes = {
    "BTN_SOUTH": 0,   # A
    "BTN_EAST": 1,    # B
    "BTN_NORTH": 2,   # X
    "BTN_WEST": 3,    # Y
    "BTN_TL": 4,      # LB
    "BTN_TR": 5,      # RB
    "BTN_THUMBL": 6,  # 左摇杆按下
    "BTN_THUMBR": 7,  # 右摇杆按下
    "BTN_SELECT": 8,  # Select
    "BTN_START": 9,   # Start
    "BTN_MODE": 10,   # Xbox按钮
    "ABS_X": 11,      # 左摇杆水平
    "ABS_Y": 12,      # 左摇杆垂直
    "ABS_RX": 13,     # 右摇杆水平
    "ABS_RY": 14,     # 右摇杆垂直
    "ABS_Z": 15,      # LT
    "ABS_RZ": 16      # RT
}

# 主循环
def main():
    while True:
        events = inputs.get_gamepad()
        for event in events:
            if event.ev_type == "Key" and event.code in button_codes:
                button = event.code
                value = event.state
                if value == 1:
                    print(f"Button {button} pressed. Corresponding number: {button_codes[button]}")

if __name__ == "__main__":
    main()
