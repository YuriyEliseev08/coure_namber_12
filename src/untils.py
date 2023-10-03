import funtion

dic_list = funtion.get_operatios_list("operation.json")

filtr = funtion.filtr_exequted(dic_list)

sort_list = funtion.sort_list(filtr)

for element in sort_list[:5]:
    print(funtion.get_out_putt(element))
    print()
