import math

class StatsEngine:
    def __init__(self, data_list):
        self.data = data_list
        self.count = len(data_list)

    def is_empty(self):
        return self.count == 0

    def get_basic_stats(self):
        if self.is_empty():
            return None

        return {
            "total_count": self.count,
            "sum": sum(self.data),
            "average": sum(self.data) / self.count,
            "max": max(self.data),
            "min": min(self.data)
        }

    def get_pos_neg_zeros(self):
        pos = len([x for x in self.data if x > 0])
        neg = len([x for x in self.data if x < 0])
        zeros = len([x for x in self.data if x == 0])
        return {"positive": pos, "negative": neg, "zeros": zeros}

    def get_reversed_data(self):
        return self.data[::-1]

    def get_variance_std_dev(self):
        if self.is_empty():
            return {"variance": 0, "std_dev": 0}

        avg = sum(self.data) / self.count
        variance = sum((x - avg) ** 2 for x in self.data) / self.count
        std_dev = math.sqrt(variance)

        return {"variance": variance, "std_dev": std_dev}