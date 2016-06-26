## To start server

```python
 python manage.py runserver
```

## Outline

The way that I am approaching this project:
1. Read through the api documents and call apis through a browser to understand how they work and what to behaviour to expect.
1. a)  I'll likely test it through [httpie](https://github.com/jkbrzt/httpie) as I've found it a useful tool to test apis.

2. Create a new Django project.  I'm going to use Django as we're familiar with the library.
2.a)  I'm going to use [requests](https://github.com/kennethreitz/requests) to make the get request to C42's apis since it's commonly recommended and simple to use.
2.b)  As I mentioned above I'll likely use [httpie](https://github.com/jkbrzt/httpie) and the chrome browser to test the GET requests.

3. Create the needed url in urls.py and the handler for this url.  I'll just return a example stub initially to ensure the correct endpoint is getting hit.

4. I'll create two functions to do the two api calls that are needed.

5. I'll create two helper functions that call the api functions, parse the data in response, and return the needed data.

6. I'll change my api endpoint function to get the data from the two helper functions and return the requested data rather than the stub.

7. Add caching so api response is cached.

## External Libraries

[Django](https://www.djangoproject.com/)

[Requests](http://docs.python-requests.org/en/master/) *Use ```pip install requests``` to install

[Memcached](http://memcached.org/) *Daemon that runs in background.
Install for linux ``` sudo apt-get install memcached ```
Install for mac OSX ``` brew install memcached ```
To run: Open an terminal and run command ``` memcached ```

[Python Memcached](https://pypi.python.org/pypi/python-memcached) *Use ``` pip install python-memcached ``` to install

[Httpie](https://github.com/jkbrzt/httpie) *Only used for testing purposes, not required
