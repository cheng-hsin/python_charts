def water_breathing_lookup(swordsman, ghost, form_number):
    """
    >>> water_breathing_lookup('炭治郎', '手鬼', 1)
    '炭治郎對手鬼使出了水之呼吸第1型水面斬'
    >>> water_breathing_lookup('富岡義勇', '蜘蛛鬼父', 4)
    '富岡義勇對蜘蛛鬼父使出了水之呼吸第4型打擊之潮'
    >>> water_breathing_lookup('炭治郎', '蜘蛛鬼母', 5)
    '炭治郎對蜘蛛鬼母使出了水之呼吸第5型旱天的甘露'
    >>> water_breathing_lookup('炭治郎', '沼鬼', 6)
    '炭治郎對沼鬼使出了水之呼吸第6型旋渦'
    >>> water_breathing_lookup('炭治郎', '下弦之五累', 10)
    '炭治郎對下弦之五累使出了水之呼吸第10型生生流轉'
    >>> water_breathing_lookup('炭治郎', '下弦之五累', 11)
    '只有富岡義勇可以使用水之呼吸第11型風平浪靜'
    >>> water_breathing_lookup('富岡義勇', '下弦之五累', 11)
    '富岡義勇對下弦之五累使出了水之呼吸第11型風平浪靜'
    """
    if swordsman == '炭治郎' and ghost == '手鬼':
        return print('炭治郎對手鬼使出了水之呼吸第'+str(form_number)+'型水面斬')
    
    if swordsman == '富岡義勇' and ghost == '蜘蛛鬼父':
        return print('富岡義勇對蜘蛛鬼父使出了水之呼吸第'+str(form_number)+'型打擊之潮')

    if swordsman == '炭治郎' and ghost == '蜘蛛鬼母':
        return print('炭治郎對蜘蛛鬼母使出了水之呼吸第'+str(form_number)+'型旱天的甘露')

    if swordsman == '炭治郎' and ghost == '沼鬼':
        return print('炭治郎對沼鬼使出了水之呼吸第'+str(form_number)+'型旋渦')

    if swordsman == '炭治郎' and ghost == '下弦之五累':
        return print('炭治郎對下弦之五累使出了水之呼吸第'+str(form_number)+'型生生流轉')

    if swordsman == '富岡義勇' and ghost == '下弦之五累':
        return print('富岡義勇對下弦之五累使出了水之呼吸第'+str(form_number)+'型風平浪靜')

water_breathing_lookup('炭治郎', '手鬼', 1)
water_breathing_lookup('富岡義勇', '蜘蛛鬼父', 4)
water_breathing_lookup('炭治郎', '蜘蛛鬼母', 5)
water_breathing_lookup('炭治郎', '沼鬼', 6)
