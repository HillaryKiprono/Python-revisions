import random

counties = ["Bungoma","Kakamega","Nakuru","Kisumu"]
print(random.choice(counties))
random.shuffle(counties)
print(counties)
print(random.randint(1,5))