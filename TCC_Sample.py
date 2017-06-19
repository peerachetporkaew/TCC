# -*- coding: UTF-8 -*-
import TCCapply as TCCapply
import re
TCCapply.GenRules()
text = "ฉันกินข้าวแล้ว12345".decode("utf-8")
notSplit = re.compile(u'([^๐-๙0-9a-zA-Z])',re.UNICODE)
notSplit2 = re.compile(u'([0-9๐-๙a-zA-Z]+)',re.UNICODE)
text = notSplit2.sub('\g<0> ',text)
text = notSplit.sub('\g<0> ',text)[:-1]
TCCtext = TCCapply.ApplyTCC(text)
print TCCtext
