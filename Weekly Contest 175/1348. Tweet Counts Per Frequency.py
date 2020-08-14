class TweetCounts:

    def __init__(self):
        self.t = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.t:
            self.t[tweetName] = [time]
        else:
            self.t[tweetName] += [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            ts = 60
        elif freq == "hour":
            ts = 60*60
        elif freq == "day":
            ts = 60*60*24
        
        result = []
        while(startTime<=endTime):
            end = min(startTime+ts, endTime + 1)
            result.append(sum(startTime <= t < end
                              for t in self.t[tweetName]))
            startTime += ts
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

