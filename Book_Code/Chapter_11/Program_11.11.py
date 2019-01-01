# Program 11.11: Write Pythonic Program to Compute the End Time of an Opera,
# While Start Time and Duration are Given


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self, duration):
        opera_hours = self.hours + duration.hours
        opera_minutes = self.minutes + duration.minutes
        opera_seconds = self.seconds + duration.seconds

        while opera_seconds >= 60:
            opera_seconds = opera_seconds - 60
            opera_minutes = opera_minutes + 1

        while opera_minutes >= 60:
            opera_minutes = opera_minutes - 60
            opera_hours = opera_hours + 1

        print(f"Opera ends at {opera_hours}:{opera_minutes}:{opera_seconds}")


def main():
    opera_start = Time(10, 30, 30)
    opera_duration = Time(2, 45, 50)
    opera_start.add_time(opera_duration)


if __name__ == "__main__":
    main()



