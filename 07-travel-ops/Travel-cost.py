im_ready            = input("Hi! introduce all requested information for travel cost, duration and distance. Are you ready?(yes/no): ")
if im_ready         == "yes":
    troller_duration_time           = int(input("Good! Introduce the troller duration time in minutes: "))
    troller_rent_cost               = 1
    troller_avg_speed               = 10
    troller_cost                    = troller_rent_cost * troller_duration_time
    
    troller_distance                = round(troller_avg_speed / 60 * troller_duration_time, 3)
    print("the troller's distance was = ", troller_distance, "km.  we spent ", troller_cost, "$ for this path part."),
    
    bus_stations               = int(input("Good! Introduce how many bus stations you rode: "))
    bus_avg_speed              = 40 
    bus_cost                   = 6
    stations_distance          = 1.22
    bus_distance               = bus_stations * stations_distance 
    bus_path_time              = round(bus_distance / bus_avg_speed, 3) # in hours 
    bus_path_time              = bus_path_time * 60     # in minutes 
    bus_path_time              = round(bus_path_time + bus_stations * 2  ,2)  # ,2) waiting time on each station
    print("you rode: ", bus_stations, "bus stations. ", bus_distance, "km, and spent ", bus_path_time, " minutes  and ", bus_cost, "$ for this trip")
    
    metro_stations               = int(input("Good! Introduce how many metro stations you rode: "))
    metro_avg_speed              = 80 
    metro_cost                   = 10
    metro_stations_distance      = 5.9
    metro_distance               = metro_stations * metro_stations_distance 
    metro_path_time              = round(metro_distance / metro_avg_speed, 3) # in hours 
    metro_path_time              = metro_path_time * 60     # in minutes 
    metro_path_time              = round(metro_path_time + metro_stations * 3 ,2)   # waiting time on each station
    print("you rode: ", metro_stations, "metro stations. ", metro_distance, "km, and spent ", metro_path_time, " minutes  and ", metro_cost, "$ for this trip")
    
    total_travel_duration = round(troller_duration_time + bus_path_time + metro_path_time, 1)
    total_travel_cost     = troller_cost + bus_cost + metro_cost
    total_travel_len      = round(troller_distance + bus_distance + metro_distance, 1)

    print("let me calculate everything... :")
    print("total trip duration was ", total_travel_duration, " minutes, total distance was ", total_travel_len, "km, total trip cost was", total_travel_cost, "$" )

else:
    print("I undarstand, try it later.")

