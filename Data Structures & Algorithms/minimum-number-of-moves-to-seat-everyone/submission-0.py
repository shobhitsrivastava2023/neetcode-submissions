class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        # sorted ->> [1,4,5,9] sorted_students -> [1,2,3,6]
        seats.sort() 
        students.sort() 
        total = 0 

        for i in range(len(seats)): 
            if students[i] != seats[i]:
                total += abs(seats[i] - students[i])
            else: 
                continue
        return total 

        