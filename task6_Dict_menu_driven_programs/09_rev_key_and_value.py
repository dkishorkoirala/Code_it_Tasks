dict_ = {}

for i in range(3):
    key = input("Enter the Nepali word: ")
    value = input("Enter the English meaning: ")
    dict_[key] = value
    
print(dict_)
reverse_dict = {v: k for k, v in dict_.items()}
print(reverse_dict)