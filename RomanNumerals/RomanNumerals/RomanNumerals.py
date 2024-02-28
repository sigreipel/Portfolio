# Svetlana Greipel
# Description: Takes in an input value and converts the value to either a roman numeral or an integer.
class RomanNumeralConversion:

    def convertToRomanNumeral(self, number):
        if number == str or number <= 0 or number >= 4000:                        # Test for str, 0 or negatives, or greater than 4000
            raise Exception('The entered value cannot be converted to a roman numeral.')

        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  # lists num and conv are the same length
        conv = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_conv = ""
        for i in range(len(num_list)):
            while number >= num_list[i]:
                number = number - num_list[i]
                roman_conv = roman_conv + conv[i]
        return roman_conv

    def convertToInteger(self, roman_numeral):
        num_list = [900, 1000, 400, 500, 90, 100, 40, 50, 9, 10, 4, 5, 1]  # lists num and conv are the same length
        conv = ["CM", "M", "CD", "D", "XC", "C", "XL", "L", "IX", "X", "IV", "V", "I"]

        value = any(ele in roman_numeral for ele in conv)
        if value != True:                                                         # Test for EX: "20"
            raise Exception("The value cannot be converted into a integer.")

        if roman_numeral == "" or roman_numeral == int:                           # Test for empty string or integer
            raise Exception("The value cannot be converted into a integer.")

        number = 0
        blacklist = [0, 2, 4, 6, 8, 10]

        for i in range(len(num_list)):
            count = 0
            while conv[i] in roman_numeral:
                number = number + num_list[i]
                if i in blacklist:
                    roman_numeral = roman_numeral[2:]
                    count += 1
                else:
                    roman_numeral = roman_numeral[1:]
                    count += 1
                if count > 3:                                                     # Test for valid roman numerals
                    raise Exception("The value cannot be converted into a integer.")
        return number


if __name__ == "__main__":
    conversion = RomanNumeralConversion()
    int_value = 63
    print("You entered: {} \nThe roman numeral conversion: {}".format(int_value,conversion.convertToRomanNumeral(int_value)))
    rm_value = "LXIII"
    print("You entered: {} \nThe integer conversion: {}".format(rm_value,conversion.convertToInteger(rm_value)))
