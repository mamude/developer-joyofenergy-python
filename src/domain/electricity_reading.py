from dataclasses import dataclass


@dataclass
class ElectricityReading:
    day: str
    time: int
    reading: float

    def __init__(self, json):
        self.day = json["day"]
        self.time = json["time"]
        self.reading = json["reading"]

    def to_json(self):
        return {
            "day": self.day,
            "time": self.time,
            "reading": self.reading,
        }
