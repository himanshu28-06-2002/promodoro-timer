import time
import os
import sys
import platform

def beep():
    """Cross-platform simple sound alert."""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        print('\a')  # ASCII Bell character

def countdown(minutes, label=""):
    total_seconds = minutes * 60
    try:
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            timer = f"{label} ⏳ {mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1
        print(f"{label} ⏰ 00:00")  # Final display
    except KeyboardInterrupt:
        print("\n⏹️ Timer interrupted.")
        sys.exit()

def pomodoro(cycles=4, work_duration=25, break_duration=5, sound=True):
    for i in range(1, cycles + 1):
        print(f"\n🍅 Pomodoro {i} - Work for {work_duration} minutes")
        countdown(work_duration, label=f"Work {i}")
        print("✅ Work session complete!")
        if sound: beep()

        if i != cycles:
            print(f"\n🛌 Break Time - {break_duration} minutes")
            countdown(break_duration, label=f"Break {i}")
            print("⏰ Break over! Back to work!")
            if sound: beep()

    print("\n🎉 All Pomodoro cycles complete! Great job!")
    if sound: beep()

def get_user_input(prompt, default):
    try:
        user_input = input(prompt)
        return int(user_input) if user_input.strip() else default
    except ValueError:
        print("⚠️ Invalid input, using default.")
        return default

if __name__ == "__main__":
    print("🔔 Welcome to the Enhanced Pomodoro Timer")
    try:
        cycles = get_user_input("How many Pomodoro cycles? (default: 4): ", 4)
        work = get_user_input("Work duration in minutes? (default: 25): ", 25)
        brk = get_user_input("Break duration in minutes? (default: 5): ", 5)

        sound_pref = input("Enable sound alerts? (Y/n): ").strip().lower()
        sound = False if sound_pref == 'n' else True

        pomodoro(cycles=cycles, work_duration=work, break_duration=brk, sound=sound)
    except KeyboardInterrupt:
        print("\n⏹️ Exiting. Stay focused!")
