class Matrix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "\n".join([' '.join(map(str, line)) for line in self.value])


    def __add__(self, other):
        answer = ''
        if len(self.value) == len(other.value):
            for line_1, line_2 in zip(self.value, other.value):
                if len(line_1) != len(line_2):
                    return "Size of arrays is not equal"

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ''.join(map(str, sum_line)) + "\n"
        else:
            return "Size of arrays is not equal"
        return answer

matrix_1 = Matrix([[3, 5], [8, 7]])
matrix_2 = Matrix([[9, 1], [4, 17], [5, 5]])
print(matrix_1 + matrix_2)
