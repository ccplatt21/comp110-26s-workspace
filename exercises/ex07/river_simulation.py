__author__ = "730672284"

from exercises.ex07.river import River

my_river: River = River(10, 2)

# Print the river day and populations
print(my_river)

# Create two rivers
river_one = River(5, 1)
river_two = River(10, 2)

# Test __add__
combined_river = river_one + river_two
print(combined_river)  # Should show 15 fish, 3 bears

# Test __mul__
scaled_river = river_one * 3
print(scaled_river)  # Should show 15 fish, 3 bears
