travel_data = {
    "Hyderabad": {
        "places": ["Charminar", "Golconda Fort", "Ramoji Film City"],
        "food": ["Hyderabadi Biryani", "Haleem"],
        "cost": 5000
    },

    "Vijayawada": {
        "places": ["Kanaka Durga Temple", "Bhavani Island", "Prakasam Barrage"],
        "food": ["Andhra Meals", "Pulihora"],
        "cost": 3000
    }
}

city = input("Enter City: ")
days = int(input("Enter Number of Days: "))
budget = int(input("Enter Budget: "))

if city in travel_data:

    data = travel_data[city]

    print("\nTravel Plan")
    print("------------------")

    print("Destination:", city)
    print("Days:", days)

    print("\nPlaces to Visit:")
    for place in data["places"]:
        print("-", place)

    print("\nFood Recommendations:")
    for item in data["food"]:
        print("-", item)

    print("\nEstimated Cost:", data["cost"])

    if budget >= data["cost"]:
        print("Budget Status: Within Budget")
    else:
        print("Budget Status: Budget Insufficient")

else:
    print("City not available in knowledge base.")
