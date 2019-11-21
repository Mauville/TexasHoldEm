# Test pairs
from Texas.cards import getpairs, three, straight, samesuit, full, poker

print("######## Testing functions ########")

assert getpairs([1, 2, 3, 4, 4]) == 0
assert getpairs([1, 1, 3, 4, 9]) == 0

# Test no pairs
assert getpairs([1, 0, 3, 4, 9]) == -1
assert getpairs([1, 0, 3, 4, 9]) == -1

# Test two pairs
assert getpairs([1, 1, 3, 3, 9]) == 1
assert getpairs([0, 1, 1, 3, 3]) == 1

# Test three
assert not three([1, 2, 3, 4, 5])[0]
assert three([1, 1, 1, 4, 5])[0]
assert three([1, 2, 2, 2, 5])[0]
assert three([1, 2, 3, 3, 3])[0]

# test straight
assert straight([1, 2, 3, 4, 5])
assert straight([12, 13, 14, 15, 16])
assert not straight([1, 3, 4, 5, 6])
assert not straight([1, 2, 3, 4, 6])
# THIS CASE SHOULD WORK
# assert straight([51, 1, 2, 3, 4]) == True

# Test flush
assert samesuit([{"suit": "♠"}, {"suit": "♠"}, {"suit": "♠"}, {"suit": "♠"}])
assert samesuit([{"suit": "♥"}, {"suit": "♥"}, {"suit": "♥"}, {"suit": "♥"}])
assert samesuit([{"suit": "♦"}, {"suit": "♦"}, {"suit": "♦"}, {"suit": "♦"}])
assert samesuit([{"suit": "♣"}, {"suit": "♣"}, {"suit": "♣"}, {"suit": "♣"}])
assert not samesuit([{"suit": "♥"}, {"suit": "♣"}, {"suit": "♣"}, {"suit": "♣"}])
assert not samesuit([{"suit": "♦"}, {"suit": "♦"}, {"suit": "♦"}, {"suit": "♣"}])

# Test Full
assert full([1, 1, 2, 2, 2])
assert full([1, 1, 1, 2, 2])
assert not full([1, 1, 3, 2, 2])
assert not full([1, 1, 1, 3, 2])

# Test Poker
assert poker([1, 1, 1, 1, 5])
assert poker([5, 1, 1, 1, 1])
assert not poker([5, 1, 1, 1, 5])
assert not poker([2, 1, 1, 1, 5])
print("######## DONE ########")
