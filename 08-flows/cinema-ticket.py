from os import system
# data
m_tittle_1  = "Avatar 2"
m_tittle_2  = "Terminator 7"
m_tittle_3  = "Titanic Zombie"
m_1_t_cost_a = 100
m_1_t_cost_b = 120
time_1      ="18.00"
time_2      ="20.00"
cost=0
system("cls")
#movie board
print(
    f"""
1.  {m_tittle_1}
    a.  {time_1}
    b.  {time_2}
2.  {m_tittle_2}
    a.  {time_1}
    b.  {time_2}
3.  {m_tittle_3}
    a.  {time_1}
    b.  {time_2}
    """
)
#Input from client
try:
    movie_number    =   int(input("choise a movie (1/2/3):"))
    if movie_number == 1:
        print(f"You  chosen '{m_tittle_1}'")
        time    = input("Choose time(a/b):")
        if time == "a":
            print(f"time {time_1}, ticket cost: {m_1_t_cost_a}")
            cost =  m_1_t_cost_a
        elif time == "b":
            print(f"time {time_2}, ticket cost: {m_1_t_cost_b}")
            cost =  m_1_t_cost_b
        else:
            quit("choose a or b only")
        try:
            amount = int(input("How many tickets would you like?: "))
            total = amount*cost
            print(f"You should pay : {amount} x {cost} = {total} $")
            buy_accept  = input(" Do you accept it (yes/no)?: ")
            if buy_accept == "yes":
                print("Thank you and enjoy!")
            else:
                print("oh, try again.")
        except:
            print("only digits please")
    elif movie_number == 2: 
        print(f"You  chosen '{m_tittle_2}'")
        time    = input("Choose time(a/b):")
        if time == "a":
            print(f"time {time_1}, ticket cost: {m_1_t_cost_a}")
            cost =  m_1_t_cost_a
        elif time == "b":
            print(f"time {time_2}, ticket cost: {m_1_t_cost_b}")
            cost =  m_1_t_cost_b
        else:
            quit("choose a or b only")
        try:
            amount = int(input("How many tickets would you like?: "))
            total = amount*cost
            print(f"You should pay : {amount} x {cost} = {total} $")
            buy_accept  = input(" Do you accept it (yes/no)?: ")
            if buy_accept == "yes":
                print("Thank you and enjoy!")
            else:
                print("oh, try again.")
        except:
            print("only digits please")
    elif movie_number == 3:
        print(f"You  chosen '{m_tittle_3}'")
        time    = input("Choose time(a/b):")
        if time == "a":
            print(f"time {time_1}, ticket cost: {m_1_t_cost_a}")
            cost =  m_1_t_cost_a
        elif time == "b":
            print(f"time {time_2}, ticket cost: {m_1_t_cost_b}")
            cost =  m_1_t_cost_b
        else:
            quit("choose a or b only")
        try:
            amount = int(input("How many tickets would you like?: "))
            total = amount*cost
            print(f"You should pay : {amount} x {cost} = {total} $")
            buy_accept  = input(" Do you accept it (yes/no)?: ")
            if buy_accept == "yes":
                print("Thank you and enjoy!")
            else:
                print("oh, try again.")
        except:
            print("only digits please")
    else:
        print("choose only from 1 to 3")
except:
    quit("Wrong input data, try again pls." )


