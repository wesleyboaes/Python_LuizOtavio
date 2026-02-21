"""
CONSTANT = "Variables" that won'n change.
Many conditions in the same if (bad).
    <- Complexity count (bad).
"""
speed = 59 # Actual car speed
car_position = 98 # Car position on the road

RADAR_1 = 60 # Maximum speed of radar 1
POSITION_1 = 100 # Position of radar 1
RADAR_RANGE = 1 # Range of the radar

spd_limit_exceeded = speed > RADAR_1
car_on_radar_range = (POSITION_1 - RADAR_RANGE) <= car_position and (POSITION_1 + RADAR_RANGE) >= car_position
car_fined = car_on_radar_range and spd_limit_exceeded

if car_fined:
    print('The car was fined')

if spd_limit_exceeded:
    print('Car speed exceeded radar limit')

if car_on_radar_range:
    print('Car passed through the radar')