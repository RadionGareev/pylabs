#online food order
delivery_free_limit     = 500.00
order_cost              = 700.00
delivery_cost           = 100.00
delivery_wants          = input('dou you want delivery? (yes/no)')
client_want_delivery    = delivery_wants == 'yes'
client_is_vip           = False
delivery_free_cost      = order_cost > delivery_free_limit
delivery_is_free        = client_want_delivery and (client_is_vip or delivery_free_cost)
delivery_is_free and print('you got free delivery')
not delivery_is_free and print('you got to pay ', delivery_cost, "for delivery")