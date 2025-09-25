

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        numbers_split = numbers.split(",")
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
