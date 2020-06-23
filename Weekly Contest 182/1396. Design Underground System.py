class UndergroundSystem:

    def __init__(self):
        self.l = {}
        self.track = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.l:
            self.l[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.l:
            start_place, start_time = self.l[id] 
            self.l.pop(id, None)
            if (start_place,stationName) not in self.track:
                self.track[(start_place,stationName)] = [(t-start_time), 1]
            else:
                self.track[(start_place,stationName)][0] += (t-start_time)
                self.track[(start_place,stationName)][1] += 1
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.track:
            ans = self.track[(startStation,endStation)]
            return ans[0]/ans[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

