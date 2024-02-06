#student addmision application

#input data
studen_scook_mark       =   7.0
university_mark         =   7.0
university_contract     =   10000 # int /year
student_money           =   2000 # 
student_dad_has_conn    = True
# Locica de admitere
approove                = studen_scook_mark >= university_mark\
                            and\
                            student_money >= university_contract\
                            or student_dad_has_conn == True
#approove                = university_contract <= student_money # Bool
#output
print("studentul e admis?", approove)

