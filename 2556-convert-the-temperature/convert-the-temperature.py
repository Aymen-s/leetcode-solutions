class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = []
        kelvin = celsius + 273.15
        arr.append(kelvin)
        fahrenheit = celsius * 1.80 + 32.00
        arr.append(fahrenheit)
        return arr
        