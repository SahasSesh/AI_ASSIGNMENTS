# Simple Bayesian Network Example

P_cloudy = 0.5

P_rain_given_cloudy = 0.8
P_rain_given_not_cloudy = 0.2

P_wet_given_rain = 0.9
P_wet_given_not_rain = 0.1

# Probability of Rain
P_rain = (
    P_rain_given_cloudy * P_cloudy
    +
    P_rain_given_not_cloudy * (1 - P_cloudy)
)

# Probability of Wet Grass
P_wet = (
    P_wet_given_rain * P_rain
    +
    P_wet_given_not_rain * (1 - P_rain)
)

print("Bayesian Network Example")
print("------------------------")
print("P(Cloudy) =", P_cloudy)
print("P(Rain) =", round(P_rain, 2))
print("P(Wet Grass) =", round(P_wet, 2))
