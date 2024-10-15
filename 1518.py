class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles  # Start by drinking the initial bottles
        
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange  # Bottles you can exchange
            remainder = numBottles % numExchange  # Remaining unexchangeable bottles
            result += new_bottles  # Drink the new bottles
            numBottles = new_bottles + remainder  # Update with new and leftover bottles
        
        return result