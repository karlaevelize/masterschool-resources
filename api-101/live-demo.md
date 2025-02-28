# API 101 - Live Demo

During the Live Demo, we want to show how to find API's and how to work them. When it comes to working with APIs, we will use the `requests` library, but ut's important to let students know that there are other ways of doing this.

## Finding APIs

There are many ways to find APIs. The first thing you have to do is to decide what you want to do with the API. Once you know what you want to do, you can search for APIs that do that.

Suppose we want to build an application that shows the user a random joke. We can search for "random quote API" and we will find the [Zen Quotes](https://zenquotes.io/).

If you check the documentation, you will see that you can get a random quote by making a GET request to `https://zenquotes.io/api/random`. That's the URL we will use in our code.

## Working with APIs

To work with APIs, we will use the `requests` library. This library allows us to make HTTP requests in Python. To install it, you can run `pip install requests`, don't forget set up your virtual environment before.

Let's see how we can get a random quote using the `requests` library.

```python
import requests

response = requests.get("https://zenquotes.io/api/random")
# Show the students what happens when you only print the response
print(response)
# Show the students what happens when you print the response to json
print(response.json())
# Show them how to get the quote
quote = response.json()[0]['q'] 
print(quote)
```

This code will make a GET request to the Zen Quotes API and print a random quote. You can run this code in your terminal and see the result.

Using the same API, we can also get a list of 50 quotes. To do that, we need to make a GET request to `https://zenquotes.io/api/quotes`.

```python
response = requests.get("https://zenquotes.io/api/quotes")
quotes = response.json()
for quote in quotes:
    print(quote['q'])
```

This code will print 50 quotes from the Zen Quotes API.

And finally we can also get the quote of the day. To do that, we need to make a GET request to `https://zenquotes.io/api/today`.

```python
response = requests.get("https://zenquotes.io/api/today")
quote = response.json()[0]
print(quote['q'])
```