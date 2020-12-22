def merge_forname(the_input, first, middle, last):
    left = the_input[first:middle + 1]
    right = the_input[middle + 1:last + 1]

    left_splited = the_input[first:middle + 1]
    right_splited = the_input[middle + 1:last + 1]
    for j in range(len(left_splited)):
        left_splited[j] = str(left_splited[j]).split(' | ')
    for k in range(len(right_splited)):
        right_splited[k] = str(right_splited[k]).split(' | ')

    l = r = 0
    for i in range(first, last + 1):
        if l >= len(left):
            the_input[i] = right[r]
            r += 1
        elif r >= len(right):
            the_input[i] = left[l]
            l += 1
        elif left_splited[l][0] <= right_splited[r][0]:
            the_input[i] = left[l]
            l += 1
        elif left_splited[l][0] > right_splited[r][0]:
            the_input[i] = right[r]
            r += 1


def recursion_forname(the_input, first, last):
    if first < last:
        middle = first + (last - first) // 2
        recursion_forname(the_input, first, middle)
        recursion_forname(the_input, middle + 1, last)
        merge_forname(the_input, first, middle, last)


def merge_sort_forname(the_input):
    recursion_forname(the_input, 0, len(the_input) - 1)


def merge_formark(the_input, first, middle, last):
    left = the_input[first:middle + 1]
    right = the_input[middle + 1:last + 1]

    left_splited = the_input[first:middle + 1]
    right_splited = the_input[middle + 1:last + 1]
    for j in range(len(left_splited)):
        left_splited[j] = str(left_splited[j]).split(' | ')
    for k in range(len(right_splited)):
        right_splited[k] = str(right_splited[k]).split(' | ')

    l = r = 0
    for i in range(first, last + 1):
        if l >= len(left):
            the_input[i] = right[r]
            r += 1
        elif r >= len(right):
            the_input[i] = left[l]
            l += 1
        elif float(left_splited[l][0]) >= float(right_splited[r][0]):
            the_input[i] = left[l]
            l += 1
        elif float(left_splited[l][0]) < float(right_splited[r][0]):
            the_input[i] = right[r]
            r += 1


def recursion_formark(the_input, first, last):
    if first < last:
        middle = first + (last - first) // 2
        recursion_formark(the_input, first, middle)
        recursion_formark(the_input, middle + 1, last)
        merge_formark(the_input, first, middle, last)


def merge_sort_formark(the_input):
    recursion_formark(the_input, 0, len(the_input) - 1)


class Feedback:  # клас-звіт, що надає статистичні дані
    def __init__(self, name_of_test, qst_amount):
        self.file = open('{}_answers.txt'.format(name_of_test), 'r')
        self.qst_amount = qst_amount - 1
        self.name = name_of_test
        self.data = self.file.readlines()
        self.file.close()

        self.block = (self.qst_amount * 3) + 4

    def sort_by_name(self):  # створює новий файл, де респонденти відсортовані по іменам
        new_file = open('{}_name-sorted.txt'.format(self.name), "w")

        arr_names = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n")
            arr_names.append(name + " | " + mark)

        merge_sort_forname(arr_names)
        for j in range(len(arr_names)):
            new_file.write(arr_names[j] + "\n")

        new_file.close()

    def sort_by_mark(self):  # створює новий файл, де респонденти відсортовані по балам
        new_file = open('{}_mark-sorted.txt'.format(self.name), "w")

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n")
            arr_marks.append(mark + " | " + name)

        merge_sort_formark(arr_marks)
        for j in range(len(arr_marks)):
            new_file.write(arr_marks[j] + "\n")

        new_file.close()

    def filter_by_mark(self, limit, less_or_more):  # показує лише результати респондентів в заданих межах балів
        lim_name = less_or_more + str(limit)
        new_file = open('{}_{}.txt'.format(self.name, lim_name), "w")

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            name = str(self.data[i]).strip("\n")
            mark = float(str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n"))
            limit = float(limit)

            if less_or_more == 'less':
                if mark <= limit:
                    arr_marks.append(str(mark) + ", " + name)
            elif less_or_more == 'more':
                if mark >= limit:
                    arr_marks.append(str(mark) + ", " + name)
            else:
                print("Run the command again and check the spelling.")
                break

        for j in range(len(arr_marks)):
            new_file.write(arr_marks[j] + "\n")

        new_file.close()

    def statistic_by_mark(self, max_mark):  # надає статистику по результатам проходження тесту
        new_file = open('{}_statistic.txt'.format(self.name), "w")

        arr_marks = []
        for i in range(2, len(self.data), self.block):
            mark = float(str(self.data[i + (self.qst_amount * 3) + 2]).strip("\n"))
            arr_marks.append(mark)

        amount_maxmark = arr_marks.count(max_mark)
        average = sum(arr_marks) / len(arr_marks)   # середній бал
        av_procent = (average * 100) / max_mark     # середня успішність у відсотках

        new_file.write("Average mark: " + str(round(average, 3)) + " from " + str(max_mark) + "\n")
        new_file.write("Average success rate in percent: " + str(round(av_procent, 3)) + "%" + "\n")
        new_file.write("Number of excellent tests: " + str(amount_maxmark) + " from " + str(len(arr_marks)))
        new_file.close()
