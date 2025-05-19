# class Cookie:
#   def __init___(self, color):
#     self.color = color
  
#   def get_color(self):
#     return self.color
  
#   def set_color(self, color):
#     self.color = color

# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('cookie one is', cookie_one.get_color())
# print('cookie two is', cookie_two.get_color())




# 2222222


# num1 = 11
# num2 = num1

# print("Before num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to: ", id(num1))
# print("num2 points to: ", id(num2))


# num2 = 22

# print("\nAfter num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to: ", id(num1))
# print("num2 points to: ", id(num2))



# 333333


dict1 = {
    'value':11
}
dict2 = dict1

print("\n\nbefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

dict2['value'] = 22

print("\nafter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))


