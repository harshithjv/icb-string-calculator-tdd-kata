import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = r",|\n"
        if numbers.startswith("//"):
            split_result = numbers[2:].split("\n")
            delimiter, numbers = split_result
            

        numbers_split = re.split(delimiter, numbers)
        sum = 0
        for number in numbers_split:
            try:
                num = int(number)
            except Exception:
                pass
            else:
                sum += num
        if sum:
            return sum

        return -1
