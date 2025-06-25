str1 = "i like this program very much"

list = str1.split()


str2 = ""
for item in list:
    str2 = item +" "+str2

#print(str2)


def reversesentence(str1):
    list = str1.split()
    rev = " "
    length = len(list) - 1
    while length >= 0:
        rev += list[length] + " "
        length-=1
    print(rev)


#reversesentence("This is my book")


def boundbytag():
    bound_by = "[[]]"
    tag_name = "tag"
    var1 = bound_by[0:2]
    var2 = bound_by[2:4]
    var3 = var1 + tag_name + var2
    print(var3)


boundbytag()