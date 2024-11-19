import json
import requests
import os
from test_data import test_data

base_url = test_data["base_url"]
auth_url = base_url + test_data["auth_endpoint"]
create_booking_url = base_url + test_data["create_booking_endpoint"]


def get_auth_token():
    try:
        username = test_data["username"]
        password = test_data["password"]

        request_body= {
            "username": username,
            "password": password
        }
        request_headers = {
            "Content-Type" : "application/json"
        }
        # The json.dumps() serializes Python objects into JSON strings
        # Without json.dumps(), the request body might be sent as a Python dictionary, which the server may not understand.
        request_body_json = json.dumps(request_body, indent=4)
        #print(f"Request Body: {request_body_json}")
        res = requests.post(auth_url,request_body_json,headers=request_headers)

        if res.status_code == 200:
            response = res.json()
            booking_id = response["token"]
            return response
        else:
            print(f"Test failed with status code: {res.status_code} ")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

def create_booking():
    try:
        depositpaid = test_data["create_booking_data"]["depositpaid"]
        totalprice = test_data["create_booking_data"]["totalprice"]
        firstname = test_data["create_booking_data"]["firstname"]
        lastname = test_data["create_booking_data"]["lastname"]
        additionalneeds = test_data["create_booking_data"]["additionalneeds"]
        checkin = test_data["create_booking_data"]["bookingdates"]["checkin"]
        checkout = test_data["create_booking_data"]["bookingdates"]["checkout"]

        create_booking_request_body= {
            "firstname" : firstname,
            "lastname" : lastname,
            "totalprice" : totalprice,
            "depositpaid" : depositpaid,#supposed to be true
            "bookingdates" : {
                "checkin" : checkin,
                "checkout" : checkout
            },
            "additionalneeds" : additionalneeds
        }
        request_headers = {
            "Content-Type" : "application/json"
        }
        # The json.dumps() serializes Python objects into JSON strings
        #
        # Without json.dumps(), the request body might be sent as a Python dictionary, which the server may not understand.
        create_booking_request_body_json = json.dumps(create_booking_request_body, indent=4)
        #print(f"Request Body: {create_booking_request_body_json}")
        res = requests.post(create_booking_url,create_booking_request_body_json,headers=request_headers)
        if res.status_code == 200:
            response = res.json()
            booking_id = response["bookingid"]
            return response
        else:
            print(f"Test failed with statusCode: {res.status_code}")
            return res.text

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")


print(get_auth_token())
#if __name__ == "__main__":
 #   get_all_products()