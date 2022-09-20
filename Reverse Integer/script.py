from venv import create


class Solution(object):
    def reverse(x):
        if x >= 0:
            xs = str(x)
            if xs == '0':
                return int(xs)
            create_list = list(reversed(xs))
            if create_list[0] == '0':
                ehh = ''.join(create_list)
                removed_value = ehh.strip('0')
                final = removed_value
            else:
                final = ''.join(create_list)
            if int(final) > 2147483647:
                print(final)
                return 0
            else:
                print(final)
                return final
        else:
            xs = str(x)
            removed_value = xs.strip('-')
            almost = list(reversed(removed_value))
            if almost[0] == '0':
                ehh = ''.join(almost)
                removed_value2 = ehh.strip('0')
                final = '-' + removed_value2
            else:
                ehh = ''.join(almost)
                final = '-' + ehh
            if int(final) < -2147483647:
                print(final)
                return 0
            else:
                print(final)
                return final

Solution.reverse(-123)
