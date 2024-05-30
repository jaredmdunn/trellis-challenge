from ninja import NinjaAPI, Schema
import time

from numstowords.utils import convert_num_to_english

api = NinjaAPI()

class NumberInEnglish(Schema):
    """A Ninja Schema for the output of both API routes."""
    status: str
    num_in_english: str = None

@api.get("/num_to_english")
def get_num_to_english(request, num: int) -> NumberInEnglish:
    """GET route for converting a number to English right away.

    Args:
        num (int): The number (integer) to convert to English.

    Returns:
        NumberInEnglish: An object with the converted number and a status message.
    """
    try:
        english = convert_num_to_english(num)
        return NumberInEnglish(status="ok", num_in_english=english)

    except ValueError as err:
        return NumberInEnglish(status=f"Improper input: {err}")

    except Exception as e:
        return NumberInEnglish(status=f"Oops! Something went wrong!: {e}")

class NumberParam(Schema):
    """A Ninja Schema for posting numbers."""
    number: int

@api.post("/num_to_english")
def post_num_to_english(request, num: NumberParam) -> NumberInEnglish:
    """POST route for converting a number to English after a 5 second delay.

    Args:
        num (int): The number (integer) to convert to English.

    Returns:
        NumberInEnglish: An object with the converted number and a status message.
    """
    time.sleep(5) # wait 5 seconds

    try:
        english = convert_num_to_english(num.number)
        return NumberInEnglish(status="ok", num_in_english=english)

    except ValueError as err:
        return NumberInEnglish(status=f"Improper input: {err}")

    except Exception as e:
        return NumberInEnglish(status=f"Oops! Something went wrong!: {e}")

