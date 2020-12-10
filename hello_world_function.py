def hello_world():
    response = "Hello World!"
    return response

    # print(hello_world())

    username = input("What is your name?")

    greeting = hello_world(username)
    
    print(greeting)