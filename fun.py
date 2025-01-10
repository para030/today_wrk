from jsonutils import*
def stud_reg( name,age,course,address):
    data=read_json()
    stud_dict={
        
        "sno":len(data["students"])+1,
        "name":name,
        "age":age,
        "course":course,
        "address":address 
    }
    data["students"].append(stud_dict)
    write_json(data)
    
    
    

def update_stud(id,name,age,course,address):
    data=read_json()
    for stud in data["students"]:
        if str (stud["sno"]) == id:
            stud ["name"]=name
            stud["age"]=age
            stud["course"]=course
            stud["address"]=address
            break
    write_json(data)


def delete_stud(id):
    data=read_json()
    for stud in data["students"]:
        if str(stud["sno"]) == id:
            print(stud)
            data["students"].remove(stud)
            break
    i=1
    for stud in data["students"]:
       stud["sno"]=i
       i+=1
    write_json(data)

        
    
    
        
