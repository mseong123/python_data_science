# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: melee <melee@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 14:46:36 by melee             #+#    #+#              #
#    Updated: 2023/09/18 16:23:35 by melee            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
	if len(sys.argv) > 1 and sys.argv[1] != "0":
		int(sys.argv[1])
except AssertionError as message:
	print(message)
except ValueError:
	print("AssertionError: argument is not an integer")
else:
	if len(sys.argv) == 1:
		print("")
	elif int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	elif int(sys.argv[1]) % 2 == 1:
		print("I'm Odd.")