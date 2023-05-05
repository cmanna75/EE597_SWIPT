import random
for i in range(0,60):
  x = random.randint(1,999)
  y = random.randint(1,999)
  print("<device id=\"{}\" name=\"n{}\" icon=\"/home/ee597/EE597_SWIPT/icons/zebra.jpeg\" type=\"PC\" class=\"\" image=\"\">".format(i+11,i+11))
  print("  <position x=\"{}\" y=\"{}\" lat=\"47.57795444370553\" lon=\"-122.13052758818174\" alt=\"2.0\"/>".format(x,y))
  print("  <services>")
  print("    <service name=\"DefaultRoute\"/>")
  print("  </services>")
  print("</device>")
