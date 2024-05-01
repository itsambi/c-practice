def is_leap(year):
    leap = False
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return leap

year = int(input())
print(is_leap(year))


if __name__ == '__main__':
    n = int(input())
    xy = range(1,n+1)
    for i in xy:
        print(i, end="")