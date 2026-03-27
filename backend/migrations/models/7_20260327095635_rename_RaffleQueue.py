from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return "SELECT 1;"


async def downgrade(db: BaseDBAsyncClient) -> str:
    return "SELECT 1;"


MODELS_STATE = (
    "eJztmm1z2jgQgP8Kw6fcTK5jjN+4b+RtmmsTUkLvblo6HtmWiSdGJrLclOvkv59WtrExNr"
    "FTArTHlwR2V7L0aLW7kvnengYO9sM3N4gyz/ZmiLD2H63vbYKmmH8oUx+32mg2y5QgYMjy"
    "hf0sMxQKZIWMIhs6dZEfYi5ycGhTb8a8gECLcaR2bXkcKVjC40iTLYdLeqo2jnTNUEBuIS"
    "5RVAP+SqDtqir07QQ279wjE94NiXyfiyLiPUTYZMEEsztMueLzFy72iIO/4TD9Ors3XQ/7"
    "ztJMPQf6FHKTzWdCdknYhTCEp1mmHfjRlGTGszm7C8jC2ovhTDDBFDEM3TMawZRhdAmhlE"
    "I80swkHmKujYNdFPksm9syt1S4ysAOCDD3YAVgghN4yu9yR9EVo6spBjcRI1lI9Kd4etnc"
    "44aCwPWo/ST0iKHYQmDMuIn/K+RO7xAtR5faF+DxIRfhpajW0UsFGb7Mzdbyaxc8q+d0Y/"
    "+q8Kwi1Sn6ZvqYTNgd/6pKaxD+1R+evu0Pj1TpN+g74Nsh3ivXiUYWKqCcUbX51mpCNbXf"
    "PVXVwSrsUVffD5JeaDoUPZJVmidB4GNEKnZ4rlkBqsXbvRbVyiCpabILDiprgNiV86GyHu"
    "g1YE8Gg/fQyTQMH3whuBwVCH+8OjkfHnUEeG7kMZwPDznHpRiQmIitAj/jGuZNcYULL7Us"
    "MHeSpm/SD1t16/rBls/BGRB/nsTxNcxHl1fnt6P+1c0S+LP+6Bw0spDOC9IjreD4i05af1"
    "+O3rbga+vT4PpcEAxCNqHiiZnd6FMbxoQiFpgkeDSRk0s5qTQF8wTJ0r3PhX0QWMi+f0TU"
    "MZc0mQdQbAfUCUv2W9Lw4t0Q+0igXV3opOAYItf18VB0tf28IC9qEMgRjbZXJk1dAJgFcl"
    "BFcVU1ladFCSJoImYBz4YnpXUZ9f7FpQWbUKwv1cCkfpGGdSjG3A5K0aiK3RlHhmXxsk13"
    "NXwoyQ4l2Q8XDznPiot9vedKLykkOlKdSoJbVZYSQrec3Hz8FfsNfHJh/7xbbodsz9B7nK"
    "mlwF+M9HHkuhLAVnAXiTOYlKrjBqAGOdR0mqXxEKDbusU/d5FRc1k24uzZGjxE/GzpsXmD"
    "Zcg32d5KdJ5zcE3VOe1ex3a3R/L/mdE1WZGW8zqswB7n9RjWhwhHpdk9r16b46kwNB8Wlj"
    "Uyff4Kpqd14NQhd6oOc4fsvvXsLuo2s2kqKrT6JRPScQuM5azH+ofjTWcpmu3QG0zDgFxH"
    "0warVdV898uWjw7xBRqksd1AhsE1qXNT+93XuXmKWtfmMdZw96jO9aYTM6Il4aWaba7Ji/"
    "AmQXgzoUVz4UwqKzycGNycS1x4lRDHDl2VDfBdA0NmU+CMgYSNrapw3ujWPPBvYR14qYRp"
    "g7CxsN+DONHtyXBrYLgpd8Mx4O7Altz0c0/XpHgNdhM/DlfDh6vhw9Xwq18Nv/5BKTlVVp"
    "6UslPns0el3Fm3zmEpf6Y0LAvCmXt4O70/h6VDzPmFYk4+meR+aGI22hyrDXdfLL3sjdOm"
    "y6H4iqAZzFyT3WP8kWu+V7lcLXXXVbwXAcXehLzDc0H5kg8MEbvslUz5z7H231WrLlGPIe"
    "8+LvJdyebkk+dTxnFNedq/Pe2fnbdX3XYTUNN+fhaXrQ01t0nLce6mdutj6tl3ZVVbollb"
    "r6HM5rk6rTpfHiqyrVdkXzENkxdFde+Wck12fHVXn+LS5ZCsqjUuh7hV5eWQ0C2na9gaDS"
    "Am5j8nwFe5XeNPZLgsH/95O7iu+pnlokkB5EfCJ/jZ8Wx23PK9kH3ZT6xrKMKsl4r/FN7R"
    "Vf+fItfT94OTYlUPHZw0e8e8+fTy9B+hQeXy"
)
