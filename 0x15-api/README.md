# 0x15. API

![N|Solid](https://process.filestackapi.com/cache=expiry:max/resize=width:1050/7WnZWlR7TgafdDesB5ow)

----
## What is a API?
see [Wikipedia](https://en.wikipedia.org/wiki/Web_API)

> A Web API is an application programming interface for either a web server or a web browser. It is a web development concept, usually limited to a web application's client-side (including any web frameworks being used), and thus usually does not include web server or browser implementation details such as SAPIs or APIs unless publicly accessible by a remote web application.

----
## Making a Get Request

In order to make a REST call, the first step is to import the python `requests` module in the current environment.


    import requests
    response = requests.get("www.dummyurl.com")


> Python also provides a way to create alliances using the as keyword.

    import requests as reqs
    response = reqs.get('https://www.google.com')

To make the first request, we will be using [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API which provides JSON response for specific item like posts, todos, and albums. So, the `/todos/1` API will respond with the details of a TODO item.


    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)
    print(response.status_code)
    print(response.text)


The execution of above snippet will provide the result:

    200
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": false
        }

The status code `200` means a successful execution of request and `response.content` will return the actual JSON response of a TODO item.


>There are many [public APIs](https://github.com/public-apis/public-apis) available to test REST calls. You can also use [Postman Echo](https://docs.postman-echo.com/?version=latest#intro) or [mocky](https://www.mocky.io/) to return customized responses and headers as well as adding a delay to the generated dummy link.


----
## Changelog
* 16-Sep-2019

----
## Thanks
* [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
* [How to use sys.argv in Python](https://www.pythonforbeginners.com/system/python-sys-argv)
* [Freecodecamp radio](https://coderadio.freecodecamp.org/)
* [markdown-js](https://github.com/evilstreak/markdown-js)