class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        counter = 0
        ans = players + trainers
        l = 0
        r = len(players)
        a = r
        while r < len(ans) and l < a:
            if ans[l] <= ans[r]:
                counter += 1
                l += 1
                r += 1
            else:
                r += 1
        return counter
        

        