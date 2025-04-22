# Exercise 1
# 1
movie_prices = {
    "Inception": 12, 
    "Avatar": 15, 
    "Moana": 8
}

# 2
movie_prices["Harry Potter"] = 12

# 3
movie_prices["Inception"] = 10

# 4
for key in movie_prices:
    pass
    # print(key)

# Exercise 2

# 1
def add_movie(title, price):
    if title in movie_prices:
        return "The movie already exists"
    
    movie_prices[title] = price
    return "Movie successfully added"

print(add_movie("Moana", 10))
print(add_movie("Test", 10))

print(movie_prices)

# 2

# 3

# 4