import codecs

decode_hex = codecs.getdecoder("hex_codec")

# for an array
#msgs = [decode_hex(msg)[0] for msg in msgs]

# for a string
theString = "b'\x7f\x00\x00\x01a\ny\x0e\x04N\xb7Q\r\xf9E\x02"
myString = decode_hex(theString)[0]

print(myString)

'''
varHexa = "b'\x7f\x00\x00\x01a\ny\x0e\x04N\xb7Q\r\xf9E\x02'"

varHexa.decode('unicode_escape')
print(varHexa)

ui = 'A'.join(map(chr, [65,66,67]))
print(ui)
'''