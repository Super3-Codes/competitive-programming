  def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        trainers.sort()
        players.sort()
        left = 0
        for i , player in enumerate(players):
            while(left < len(trainers)):
                if player <= trainers[left]:
                    count += 1
                    left += 1
                    break
                left += 1
        return count
