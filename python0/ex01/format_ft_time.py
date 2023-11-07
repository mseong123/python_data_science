# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: melee <melee@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 11:22:09 by melee             #+#    #+#              #
#    Updated: 2023/09/19 16:53:51 by melee            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import datetime

time = time.time()

print("Seconds since January 1, 1970: " + "{:,.4f}".format(time) + " or " + "{:.2e}".format(time) + " in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))