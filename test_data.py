test_data = {
    "base_url": "https://restful-booker.herokuapp.com",
    "create_booking_endpoint": "/booking",
    "username": "admin",
    "password": "password123",
    "auth_endpoint": "/auth",
    ###
    "create_booking_data": {
        "firstname": "Test",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
}