# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: melee <melee@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 13:03:55 by melee             #+#    #+#              #
#    Updated: 2023/09/19 18:59:34 by melee            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	if (object == None):
		print(f"Nothing: {object} {type(object)}")
	elif (type(object) == float):
		print(f"Cheese: {object} {type(object)}")
	elif (type(object) == int):
		print(f"Zero: {object} {type(object)}")
	elif (type(object) == str and object == ""):
		print(f"Empty: {object} {type(object)}")
	elif (type(object) == bool):
		print(f"Fake: {object} {type(object)}")
	else:
		print(f"Type not Found")
		return 1
	return 0

# from NULL_not_found import NULL_not_found

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))

