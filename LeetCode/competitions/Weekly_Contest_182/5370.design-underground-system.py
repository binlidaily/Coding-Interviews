import collections

class UndergroundSystem:

    def __init__(self):
        self.check_in = collections.defaultdict()
        self.avg_time = collections.defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in:
            start, s_time = self.check_in[id]
            interval = t - s_time
            key = start + '#' + stationName
            if key in self.avg_time:
                avg, cnt = self.avg_time[key]
                self.avg_time[key] = (float(avg * cnt + interval) / (cnt + 1), cnt + 1)
            else:
                self.avg_time[key] = (interval, 1)
            del self.check_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + '#' + endStation
        if key in self.avg_time:
            return self.avg_time[key][0]
        else:
            return 0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]