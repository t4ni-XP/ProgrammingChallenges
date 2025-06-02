num_list: list[str] = [input() for _ in range(2)]
n_str: str = num_list[0]
m_str: str = num_list[1]
n_len: int = len(n_str)
m_len: int = len(m_str) 
if n_len == m_len-1:
    n_divided: str = '0.'+n_str
elif n_len < m_len:
    n_str = n_str.zfill(m_len-1)
    n_divided: str = '0.' + n_str
else:
    n_divided = n_str[:n_len-m_len+1] + '.' + n_str[n_len-m_len+1:]
    for i in range(len(m_str)-1):
        if n_divided[-1] == "0":
            n_divided = n_divided.rstrip("0")
        elif n_divided[-1] == ".":
            n_divided = n_divided.rstrip(".")
    if n_divided[-1] == ".":
        n_divided = n_divided.rstrip(".")

print(n_divided) 