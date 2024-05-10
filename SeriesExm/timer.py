class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()  # Normalize time to ensure valid values

    def __str__(self):# Format time as HH:MM:SS
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"  

    def normalize(self):
        # Normalize seconds to ensure they don't exceed 59
        extra_minutes, self.seconds = divmod(self.seconds, 60)
        self.minutes += extra_minutes

        # Normalize minutes to ensure they don't exceed 59
        extra_hours, self.minutes = divmod(self.minutes, 60)
        self.hours += extra_hours

    def __add__(self, other):
        # Add two Time instances
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds

        # Create a new Time instance for the result
        result_time = Time(total_hours, total_minutes, total_seconds)
        result_time.normalize()  # Normalize the result to maintain valid time
        return result_time

# Example usage
time1 = Time(1, 30, 45)  # 1 hour, 30 minutes, 45 seconds
time2 = Time(2, 15, 20)  # 2 hours, 15 minutes, 20 seconds
result_time = time1 + time2  # Adds the two times
print("Result:", result_time)  # Should output: "Result: 03:46:05"
