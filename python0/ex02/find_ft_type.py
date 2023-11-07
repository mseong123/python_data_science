#object is the parameter, :any is type annotation, means can accept any type of data types
def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print("{} is in the kitchen : {}".format(object, type(object)))
    elif type(object) == dict or type(object) == set or type(object) == tuple or type(object) == list:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    else:
        print("Type not Found")
    return 42


# from find_ft_type import all_thing_is_obj

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}
# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# print(all_thing_is_obj(10))
