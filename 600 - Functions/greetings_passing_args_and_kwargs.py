def greetings(from_, to):
    print(f"{from_} greets {to}")


tuple_parameters = ("Alice", "Bob")
greetings(*tuple_parameters)

dict_parameters = {
    "from_": "Alice",
    "to": "Bob"
}
greetings(**dict_parameters)
