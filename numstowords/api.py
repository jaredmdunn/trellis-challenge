from ninja import NinjaAPI
import time

from numstowords.utils import convert_num_to_english

api = NinjaAPI()

@api.get("/num_to_english")
def get_num_to_english(request, num: int):
    english = convert_num_to_english(num)
    return {
        "num_in_english": english
    }


@api.post("/num_to_english")
def post_num_to_english(request, num: int):
    time.sleep(5) # wait 5 seconds
    
    english = convert_num_to_english(num)

    return {
        "status": "ok", 
        "num_in_english": english
    }

