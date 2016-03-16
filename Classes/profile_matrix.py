from collections import defaultdict


class ProfileMatrix:
    def __init__(self, string_list, keys):
        self.matrix = dict.fromkeys(keys, defaultdict(int))
        self.len = len(string_list[0])
        self.keys = keys
        for string in string_list:
            for index in range(self.len):
                self.matrix[string[index]][index] += 1

    def create_consensus_string(self):
        consensus_list = list()
        for index in range(self.len):
            highest_count = (0, str())
            for key in self.keys:
                if self.matrix[key][index] > highest_count[0]:
                    highest_count = (self.matrix[key][index], key)
            consensus_list.append(highest_count[1])
        return ''.join(consensus_list)

    def to_string(self):
        str_builder = list()
        for key in self.keys:
            str_builder.append(key+':')
            map(lambda index: str_builder.append(' ' + self.matrix[key][index]), range(self.len))
            str_builder.append('\n')
        return ''.join(str_builder)