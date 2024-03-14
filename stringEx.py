arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split("/"))

text = "    Text with whitespaces"

name = "gaurav"
city = "hoofddrop"
country = "NETHERLANDS"

lord = "Shree Krishna"

print(name.upper())

# in-built functions
str1 = "Hello"

str2 = "World"

# Concatinate 2 strings with space in between
result = str1 + " " + str2

print(result)


# Length of a string
print(len(arn))

# lowercase string
print(country.lower())

# UPPERCASE string
print(city.upper())

# replace string
print(lord.replace(lord[0:5],"Radha"))

# split string
print(arn.split(":"))

# string strip
print(text.strip())

# Substring the text (IMPORTANT)
quote = "Python is awesome"
substring = "is"
if substring in quote:
    print(substring, "found in the quote")
    
