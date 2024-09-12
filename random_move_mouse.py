import pyautogui
import random
import time
import keyboard
import threading

# 设置一个标志，用于退出循环
exit_flag = False

def move_mouse():
    global exit_flag
    screenWidth, screenHeight = pyautogui.size()

    while not exit_flag:
        # 生成随机的x和y坐标
        x = random.randint(0, screenWidth - 1)
        y = random.randint(0, screenHeight - 1)

        # 移动鼠标到随机位置
        pyautogui.moveTo(x, y, duration=0.5)

        # 生成一个随机的暂停时间，范围在0.5到2秒之间
        pause_time = random.uniform(0.5, 2.0)

        # 暂停随机时间后再移动
        time.sleep(pause_time)

def check_for_exit():
    global exit_flag
    while not exit_flag:
        if keyboard.is_pressed('q'):
            print("退出脚本...")
            exit_flag = True
            break
        time.sleep(0.01)  # 减少CPU占用

if(__name__=='__main__'):
    # 创建并启动鼠标移动的线程
    mouse_thread = threading.Thread(target=move_mouse)
    mouse_thread.start()

    # 主线程负责检查按键
    check_for_exit()

    # 等待退出按键检测生效时，最后一次运行的鼠标线程完整结束
    mouse_thread.join()
