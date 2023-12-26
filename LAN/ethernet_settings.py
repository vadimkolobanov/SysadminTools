# import wmi
#
#
# def set_ip_address(ip_address, subnet_mask, adapter):
#     # Изменение IP-адреса и маски подсети
#     adapter.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnet_mask])
#     print("IP-адрес успешно изменен.")
#     print(adapter.IsDynamicEnabled)
#
#
# def set_default_gateway(gateway, adapter):
#     # Изменение шлюза по умолчанию
#     gateway_metric = 1
#     adapter.SetGateways(DefaultIPGateway=[gateway], GatewayCostMetric=[gateway_metric])
#     print("Шлюз по умолчанию успешно изменен.")
#
#
# def select_network_adapter(adapters):
#     # Вывод меню выбора адаптера
#     print("Выберите адаптер:")
#     for index, adapter in enumerate(adapters, start=1):
#         print(f"{index}. {adapter.Description}")
#
#     # Получение ввода от пользователя
#     selection = input("Введите номер адаптера: ")
#
#     try:
#         selection_index = int(selection)
#         if 1 <= selection_index <= len(adapters):
#             return adapters[selection_index - 1]
#         else:
#             print("Недопустимый номер адаптера.")
#     except ValueError:
#         print("Недопустимый ввод.")
#
#     return None
#
#
# # Подключение к WMI
# c = wmi.WMI()
#
# # Получение Ethernet-адаптеров
# ethernet_adapters = []
# for adapter in c.Win32_NetworkAdapterConfiguration():
#     if not adapter.Description.startswith(("WAN", 'VMware, VirtualBox, Microsoft')):
#         ethernet_adapters.append(adapter)
# if ethernet_adapters:
#     selected_adapter = select_network_adapter(ethernet_adapters)
#     if selected_adapter:
#         # Пример использования
#         new_ip_address = '192.168.1.100'
#         new_subnet_mask = '255.255.255.0'
#         new_gateway = '192.168.1.1'
#
#         set_ip_address(new_ip_address, new_subnet_mask, selected_adapter)
#         set_default_gateway(new_gateway, selected_adapter)
# else:
#     print("Ethernet-адаптеры не найдены.")
import wmi

#List NICs by Index and Description
c = wmi.WMI()
for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=False):
   print(nic.Index, nic.Description)

#Choose which NIC to apply changes to:
nic_selection_index = c.Win32_NetworkAdapterConfiguration(Index = input('Choose Network Adapter Number on left to change: '))

#This selects the entire NIC properties -- can't just use the index value above
nic_selection_all = nic_selection_index[0]

#Will be hidden once working
print(nic_selection_all)



#Get IP Info to use on NIC
ip = input('Enter IP to use: ')
subnetmask = input('Enter Subnet Mask to use: ')
gateway = input('Enter Default Gateway to use: ')
dns = '127.0.0.1'


print(ip)
print(subnetmask)
print(gateway)

## Set IP address, subnetmask and default gateway
## Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
nic_selection_all.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask],DefaultIPGateway=[gateway],DNSServerSearchOrder=[dns],DNSDomain="my.random.domain")
nic_selection_all.SetGateways(DefaultIPGateway=[gateway])
nic_selection_all.SetDNSServerSearchOrder([dns])
nic_selection_all.SetDNSDomain("my.random.domain")