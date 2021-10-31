"""Use the help function to see what each function does.
Delete this when you are done."""
help(dir)
help(hasattr)
help(id)


class Vehicle:
    """# Define the Vehicle class."""
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        """return car properties"""
        desc_str = f"{self.name} is a {self.color}s {self.kind} worth {self.value}."
        return desc_str


# Print a list of all attributes of the Vehicle class.
# Your code goes here
print(Vehicle.__dict__)
print(dir(Vehicle))
print(id(Vehicle))
