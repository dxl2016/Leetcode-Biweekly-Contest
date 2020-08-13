class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_degree = float(minutes*6)
        h_degree = (hour+minutes/60)*30
        # print(h_degree)
        # print(m_degree)
        return min(abs(h_degree-m_degree), abs(360-h_degree+m_degree), abs(360-m_degree+h_degree))

