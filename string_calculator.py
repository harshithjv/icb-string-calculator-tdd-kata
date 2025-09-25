

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        try:
            num = int(numbers)
        except Exception:
            pass
        else:
            return num
        return -1
