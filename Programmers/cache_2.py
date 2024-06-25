# There is a service which provides the information of restaurant in the specific city
# There is cache, which can store information of some cities' information(until cachesize)
# If the quaried city is in the cache -> 1, else not in the cache -> 5
# Given variables: cacheSize, cities
# Figure out the execution time of this service

class Cache():
    # init
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize      # The size of cache
        self.store = {}         # Store the information
    
    def currentSize(self):
        return len(self.store)      # The current size of cache
    
    def changePriority(self):
        # Change the priority of information
        for keys in self.store:
            self.store[keys] += 1
    
    def hit(self, key):
        # If the information is in the cache
        self.changePriority()
        self.store[key] = 1

    def miss(self, key):
        # If the information is not in the cache
        if self.currentSize() < self.cacheSize:
            # extra space exists
            self.changePriority()
            self.store[key] = 1
        else:
            # There is no extra space in this cache
            max = 0
            tem_key = ''
            for var in self.store:
                if self.store[var] > max:
                    max = self.store[var]
                    tem_key = var
            self.store.pop(tem_key)
            self.changePriority()
            self.store[key] = 1

    
    def setCache(self, key):
        # Judge hit or miss
        if key in self.store:
            self.hit(key)
            return 1    # Take 1
        else:
            self.miss(key)
            return 5    # Take 5


def solution(cacheSize, cities):
    answer = 0
    # If cacheSize is 0
    # we don't need a cache
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    # cache~~!
    cache = Cache(cacheSize)
    for city in cities:
        answer += cache.setCache(city)

    return answer
            
        
def solution_(cacheSize, cities):
    answer = 0
    cache = {}
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    for city in cities:
        # If the city is in the cache
        if city in cache:
            answer += 1
            for var in cache:
                cache[var] += 1
            cache[city] = 1
        
        # If the city is not in the cache
        else:
            answer += 5
            # smaller than cache size
            if len(cache) < cacheSize:
                for var in cache:
                    cache[var] += 1
                cache[city] = 1
            # cache is full
            else:
                tem = ''
                max = 0
                for var in cache:
                    if cache[var] > max:
                        max = cache[var]
                        tem = var
                cache.pop(tem)
                for var in cache:
                    cache[var] += 1
                cache[city] = 1

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))