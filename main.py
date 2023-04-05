#Dictionaries allow storage of K,V pairs
#Keys (such as name, age and address below MUST BE UNIQUE...SAME AS JAVA)
person = {
    "name": "Jamal",
    "age": 20,
    "address": "USA"
}
print(person["address"])
print(person.keys())
print(person.get("age"))