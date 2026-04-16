from tortoise import fields, models

class Participant(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='人员姓名')
    code = fields.CharField(max_length=50, description='工号')
    is_drawn = fields.BooleanField(default=False, description='是否已抽奖')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'participants'
        table_description = '参与抽奖的人员名单'

    def __str__(self):
        return self.name


class ParticipantSpecial(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='人员姓名')
    # 这里沿用 code 字段名复用前端现有的“编号 + 姓名”展示结构，特别大奖场景下实际存的是桌号。
    code = fields.CharField(max_length=50, description='桌号')
    position = fields.CharField(max_length=50, description='左，右')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'participants_special'
        table_description = '参与特殊大奖的人员名单'

    def __str__(self):
        return self.name


class RaffleRecord(models.Model):
    id = fields.IntField(pk=True)
    participant = fields.ForeignKeyField('models.Participant', related_name='records', description='中奖人')
    desc = fields.CharField(max_length=100, description='抽奖描述')
    name = fields.CharField(max_length=50, description='人员姓名')
    code = fields.CharField(max_length=50, description='工号')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'raffle_records'
        table_description = '中奖记录'


class RaffleQueue(models.Model):
    id = fields.IntField(pk=True)
    prize_level = fields.IntField(description='奖项等级，1为一等奖，以此类推, 0特等奖')
    raffleQueuePersonNum = fields.IntField(description='抽奖人数')
    desc = fields.CharField(max_length=100, description='抽奖描述')
    img_url = fields.CharField(max_length=100, null=True, description='图片路径，用于前端展示')
    order = fields.IntField(description='排序，越小越靠前')
    is_drawn = fields.BooleanField(default=False, description='是否已抽奖')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'raffle_queue'
        table_description = '抽奖队列'
    