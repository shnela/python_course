def greetings(from_, to):
    print(f"{from_} greets {to}")


greetings("Alice", "Bob")
greetings("Alice", to="Bob")
greetings(from_="Alice", to="Bob")
greetings(to="Bob", from_="Alice")

tuple_parameters = ("Alice", "Bob")
greetings(*tuple_parameters)

dict_parameters = {
    "from_": "Alice",
    "to": "Bob"
}