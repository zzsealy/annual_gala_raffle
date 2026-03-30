from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `lottery_queue` ADD `order` INT NOT NULL COMMENT '排序，越小越靠前';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `lottery_queue` DROP COLUMN `order`;"""


MODELS_STATE = (
    "eJztWm1v2kgQ/iuITzkpV4HxG/cN0kTNNQm5hN6dWiprba+JFbOm9ropV+W/38zaxi/YBO"
    "dCoD2kipp5We8+Ozvz7JDv7ZlvUy98c+FzToPFHxGNaPu31vc2IzN8qNQft9pkPs+0KODE"
    "9ISDF1saX5amZsgDYnFQOsQLKYhsGlqBO+euz9BlEqmSaU8ipa+ok6ivdh14lroaetu+Be"
    "4um4IhizwPRBFzYXCD+1PK72gAik+fQewym36jYfp1fm84LvXswmpcG8cUcoMv5kJ2zviZ"
    "MMS3mYble9GMZcbzBb/z2dLaZRylU8poQDjF4XkQ4aJwdgkI6TrjmWYm8RRzPjZ1SOTxbG"
    "1FZFLhKgaWzxBVmE0oFjjFt/wqdWVN1nuqrIOJmMlSoj3Gy8vWHjsKBK7G7UehJ5zEFgLG"
    "DLd54P5DDY9+pV4DAEteTyOZ4rYOylSQYZlF1Vow28sA07X+JNJMGT8p0SaR43Ss7iSSaY"
    "/gZ6eTqmMHVKOcKhCppiqD1tJMeO4RABqNpWxEdKkJ3K1sWrZJ+TN6TYPQZ1fRrMF21frv"
    "fuPy+UGmJuySqmid3cCMk1tF9eSOBNWwpvYlFGGKu0RR7VmQZXUI7Q1RnJFvcJTZlN/B12"
    "6nswazPwc3J+8GN0dg9QuO7kP6j4vDVaKSYl0RWHc2NaKgIsHUY5tzeRa8SRp+meSiOhRT"
    "gQwJRQdzkDi6nGYPTZF0jF2dYm2TYR80ImwsBbKK1u+RvdkHP7Bp0CBvLO33IE/0+hJgSn"
    "UnxV23dYIod5z0ua+pnXgPdpM/rIAiGgbhqxi/BQ13Z7Qa6KJnCW07cX2TPrwq9pszFViD"
    "PWLeIjl9a6Abn1+e3o4Hl9e4klkYfvEERIPxKWokIV2UpEdqKdKXg7T+Oh+/a+HX1sfR1a"
    "lA0A/5NBBvzOzGH9s4JxJx32D+g0HsHF9LpSkwj8g0nfscZ0KBSaz7BxLYxorGl/w621XV"
    "TJqVJYSRqdgWBBenmdDzaxJw13LnhPF2BXvPq9eS93lmGG7K3ZWeJQnWRIsVRlMx+8XVWp"
    "EVHT87qO0pyoHZ7wuzF/83qLip/e7ZTCGy+nYvjq/nVFFlkyKq1NdQZaWEWnC0GsRjar77"
    "AqrYeMlRek7d5XvLxdENDfhnB+SBreI39H2PElZzpoueJShNcN0WlvVdDVVChidLKgLrSP"
    "n8uBm8a7AbjkYXhcI4PB+XAvTD5fAU2J+IWzByOT0wkgMjqaoCAbWAxYcVRy5xPHt/Qz0i"
    "oF3d6IRl3BDH8eiNGOr1i4FUaBA0Ol6ZNA2BrXI17IpVsjShWM/P0GRzZkY1ZGBOl6TQKD"
    "L2uXTTxJuqo9IDDzvwsJdpqsaRFTN8rb9HXaWmTeufu129G1b3JYILpcsXDbYh7/J6O9F9"
    "KsCx7Qxb0rWc10Py/1nRVUnuFOs67sAe1/UCWBXlvQxmfZUPhKWR28JNqn0eKqjw2ON0Dp"
    "2W/anwh1vWT3TLyle3XNPUaHQ4Vh13zzmed5F6acIQ/+VAMzBzLruH8b9Ur61whspwXYX3"
    "zA+oO2Xv6UKgfA4TI8yqumlU/7Sw/6Faxw2Ose4+LOtdxeGExcOSadxFOxncngzenrZXw/"
    "YlQE3H+VFCdmNQc4e0Gs7d/H42oIFr3VWxtkSzlq+RzOYpnlZfLw+M7NUZ2VcahMn9Z9O2"
    "S85lx52XzVEs9FgkRdmgxwJWtT0WoSuWazwaDUBMzH9MALfSpII3clpVj3+/HV3V/Wa4dC"
    "kB+YHBAj/ZrsWPW54b8s/7CesaFHHVBfKfgnd0Ofi7jOvJxWhYZvU4wLBZ6+Tly8vjv6b6"
    "cPY="
)
