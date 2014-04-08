from sys import byteorder
if byteorder == 'litter':
  print "LittleEndian"
else:
  print "BigEndian"
