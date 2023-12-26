import datetime

class TodoItem:
    def __init__(self, text, timestamp, is_done=False):
        self.is_done = is_done
        self.text = text
        self.timestamp = timestamp

    def __str__(self):
        if self.is_done:
            return f"Done {self.text} at {self.timestamp}"
        elif self.missed():
            return f"Missed {self.text} at {self.timestamp}"
        else:
            return f"Should {self.text} at {self.timestamp}"

    def missed(self):
        return not(self.is_done) and (self.timestamp < datetime.datetime.now())

    def dump(self):
        done_part = "DONE" if self.is_done else "TODO"
        text_part = self.text
        timestamp_part = self.timestamp.strftime('%Y-%m-%d %H:%M')
        return f"{done_part} | {text_part} | {timestamp_part}"

    def get_text(self):
        return self.text

    def set_done(self):
        self.is_done = True

    @staticmethod
    def parse(input: str):
        parts = [part.strip() for part in input.split("|")]
        print(parts)
        is_done = parts[0].upper() == "DONE"
        text = parts[1]
        timestamp = datetime.datetime.strptime(parts[2], '%Y-%m-%d %H:%M')
        return TodoItem(text, timestamp, is_done)