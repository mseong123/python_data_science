"""
from time import sleep
from tqdm import tqdm
"""


def ft_tqdm(lst: range) -> None:
    """copy of tqdm"""
    lst_len = len(lst)
    count = 0
    progress = ""
    for x in lst:
        count += 1
        if (int(count / lst_len * 40) - int((count - 1) / lst_len * 40) == 1):
            progress = progress + "█"
        print(f"{(count / lst_len * 100):3.0f}%|\
{progress:40}| {count}/{lst_len}", end='\r')
        yield None


"""
for elem in ft_tqdm(range(600)):
    sleep(0.005)

for elem in tqdm(range(333)):
    sleep(0.005)
"""
