print(format("kilograms", "<15s"), format("pounds", "<15s"),
      "|", format("pounds", ">15s"), format("kilograms", ">15s"))
print("-"*65)

for x in range(10):
    kilogram = (x+1)*10
    pounds = 20+(x*15)
    print(format(kilogram, "<15d"), format(kilogram*2.2, "<15.2f"),
          "|", format(pounds, ">15d"), format(pounds*0.45, ">15.2f"))
