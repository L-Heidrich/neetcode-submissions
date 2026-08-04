class Solution:

    def is_anagram(self, str1, str2):

        record_1 = {}
        record_2 = {}

        sett = set(str1)
        sett2 = set(str2)

        for i in sett: 
            record_1[i] = 0

        for j in sett2: 
            record_2[j] = 0
        
        if record_1 != record_2:
            return False
        
        else:
            for s in str1:
                record_1[s] += 1
            for s in str2:
                record_2[s] += 1
  
        if record_1 == record_2:
            return True
        else:
            return False


            

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)

        result = [record[tuple(sorted(s))].append(s) for s in strs]
        return list(record.values())



            

