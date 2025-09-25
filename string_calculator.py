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
        negative_nums = []
        for number in numbers_split:
            try:
                num = int(number)
            except Exception:
                pass
            else:
                if num < 0:
                    negative_nums.append(str(num))
                else:
                    sum += num

        if len(negative_nums):
            raise ValueError(f"Negatives not allowed: {",".join(negative_nums)}")

        if sum:
            return sum

        return -1
