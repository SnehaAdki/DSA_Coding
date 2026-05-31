# PyJWT & jwt both packages


import jwt 
from datetime import  timedelta , timezone, datetime
import time

SECRET_KEY = "Hellow"
ALGORITHM = "HS256"

def gen_jwt(user_id, username):
    payload = {
        "pwd" : str(user_id),
        "username" : str(username),
        "exp" : datetime.now(timezone.utc) + timedelta(seconds=10),
        "iat" : datetime.now(timezone.utc)
    }

    jwt_value = jwt.encode(payload,SECRET_KEY , algorithm = ALGORITHM)
    return jwt_value

def verify(token) :
    try : 
        decoded = jwt.decode(token,SECRET_KEY, algorithms = [ALGORITHM])
        return decoded
    except jwt.ExpiredSignatureError:
        print(" Signature Expired ... ")
        return "Invaid Signaure"
    except jwt.InvalidTokenError:
        print(" Invlaid Token ... ")
        return "INvalid Token"

if __name__ == '__main__':
    print("---- Token generated  ----- ")
    my_toke = gen_jwt('123','Sneha')
    print("Generated Token ")
    print(my_toke)

    print("Success Use Case.......")
    user_details = verify(my_toke)
    if user_details:
        print("Details " , user_details)

    


    print("Invalid Token...... ")
    my_toke_update = my_toke+"abccc"
    user_details = verify(my_toke_update)
    if user_details:
        print("Details " , user_details)
    else:
        print("Error")
        print(user_details)

    time.sleep(10)
    print("Invalid Signature ")
    user_details = verify(my_toke)
    if user_details:
        print("Details " , user_details)
    else:
        print("Error")
        print(user_details)