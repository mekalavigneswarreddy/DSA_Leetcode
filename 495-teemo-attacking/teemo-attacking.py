class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if not timeSeries:
            return 0
    
        total = 0
    
        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i-1]
            total += min(gap, duration)
    
    # Add duration for last attack
        total += duration
    
        return total

        

        