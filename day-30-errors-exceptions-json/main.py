# # File not found exception
# try:  # If this thing does not work, then it moves to except
#     data = open("data.txt", "r")
#     a_dict = {"key1": "value"}
#     print(a_dict["key1"])
# except FileNotFoundError:  # If this exception occurs, it does not go further on next exceptions
#     data = open("data.txt", "a")
#     print("Creating a new data.txt")
#     data.write("Something")
# except KeyError as something:  # something = is a key that causes an error
#     print(f"That {something} key does not exist.")
#
# else:  # Occurs when everything above is fine. If at some point except occurs, else does not work.
#     print("everything went fine.")
#     content = data.read()
#     print(content)
#
# finally:  # Part of code, which will occur anyways.
#     data.close()
#     print("File 'data' has been closed.")

height = float(input("Height: "))
wight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human's height should not exceed 3 meters.")

bmi = wight / height ** 2
print(bmi)
