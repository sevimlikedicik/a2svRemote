import base64

s = b"AE/A5Qx+Hzs85/n0fkXkhV1dmTD7dNGDdbzNrGBiKE7bz9/G6or03DXXdSqV72cKf77G1ZwlgeNc4AOV+6j7YqqPvUUzahiqXpH3t2NLEaW30fxROOyTdSqX5yYVeh6xha7/pyy25gMwZjIs9ld1AUrUGmm4CIA/2kr3zxKFQAoZhJHqmRZeZ5MiiXsJ2EUOlxQx0cJVtDzclkvpsl+WdcPOgatSrU4lUMzIdEHw2bg13XElssTy5zJd22o2KCUn/w=="

decoded = base64.decodebytes(s)

print(decoded)
print(len(decoded)*8)
print("".join(["{:08b}".format(x) for x in decoded]))

