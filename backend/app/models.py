from tortoise import fields, models

class Participant(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description='人员姓名')
    code = fields.IntField(description='工号')
    is_is_drawn = fields.BooleanField(default=False, description='是否已抽奖')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'participants'
        table_description = '参与抽奖的人员名单'

    def __str__(self):
        return self.name

class Prize(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description='奖品名称')
    level = fields.IntField(description='奖项等级，1为一等奖，以此类推')
    quantity = fields.IntField(default=1, description='奖品数量')
    
    class Meta:
        table = 'prizes'
        table_description = '年会奖品设置'

    def __str__(self):
        return self.name

class RaffleRecord(models.Model):
    id = fields.IntField(pk=True)
    participant = fields.ForeignKeyField('models.Participant', related_name='records', description='中奖人')
    prize = fields.ForeignKeyField('models.Prize', related_name='records', description='所中奖品')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'raffle_records'
        table_description = '中奖记录'


class LotteryQueue(models.Model):
    id = fields.IntField(pk=True)
    prize_level = fields.IntField(description='奖项等级，1为一等奖，以此类推')
    LotteryQueuePersonNum = fields.IntField(description='抽奖人数')

    class Meta:
        table = 'lottery_queue'
        table_description = '抽奖队列'
    