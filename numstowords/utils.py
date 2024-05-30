def convert_num_to_english(num: int) -> str:
    """Takes in an integer between 0 and 1 billion (inclusive)
    and returns that number as text.

    Examples:
        4 -> "four"
        98 -> "ninety eight"
        102 -> "one hundred and 2"
        1204 -> "one thousand two hundred and four"
        12345678 -> "twelve million three hundred forty five thousand six hundred seventy eight"

    Args:
        num (int): The number to convert to text

    Returns:
        str: The English text of that number
    """

    mil = 1000000
    bil = 1000000000

    
    if num < 0 or num > bil:
        raise ValueError("The number must be between 0 and 1 billion (inclusive).")

    nums_to_words_dict: dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
        mil: "million",
        bil: "one billion",
    }

    if num in nums_to_words_dict:
        return nums_to_words_dict.get(num, "")
    
    if num < 100:
        return f"{nums_to_words_dict.get(num - num % 10, '')} {nums_to_words_dict.get(num % 10, '')}"
    
    if num < 1000:
        return f"{nums_to_words_dict.get(num // 100,'')} hundred {convert_num_to_english(num % 100)}"

    if num < mil:
        return f"{convert_num_to_english(num // 1000)} thousand {convert_num_to_english(num % 1000)}"
    
    if num < bil:
        return f"{convert_num_to_english(num // mil)} million {convert_num_to_english(num % mil)}"