#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import json

decoder = json.JSONDecoder()
def get_decoded_and_remainder(input_data):
    obj,end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj,end,remaining)

encoded_object = '[{"a":"张三","c":3.0,"b":[2,4]}]'
extra_text = 'This text is now JSON'

print 'JSON first:'
data = ''.join([encoded_object,extra_text])
obj,end,remaining = get_decoded_and_remainder(data)

print 'Object       :',obj
print 'End of parsed input:',end
print 'Remaining text :',repr(remaining)

print
print 'JSON embedded'
try:
    data = ''.join([extra_text,encoded_object,extra_text])
    obj,end,remaining = get_decoded_and_remainder(data)
except ValueError, err:
    print 'ERROR:',err