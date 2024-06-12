status_code = int(input("请输入状态码："))

match status_code:
    case 400 | 405:
        desc = "Bad Request"
    case 401 | 403 | 404:
        desc = "Not Allowed"
    case _:
        desc = "Unknown Status Code"

print("状态码描述：", desc)