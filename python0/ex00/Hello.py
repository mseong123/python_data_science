# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: melee <melee@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 10:54:50 by melee             #+#    #+#              #
#    Updated: 2023/09/18 11:05:02 by melee            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
temp_list = list(ft_tuple)
temp_list[1] = "Malaysia!"
ft_tuple = tuple(temp_list)
ft_set.remove("tutu!")
ft_set.add("KL!")
ft_dict["Hello"] = "42KL!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)