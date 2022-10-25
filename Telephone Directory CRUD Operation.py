#Telephone Directory CRUD Operation

import pymongo



client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

myDB=client.TelephoneDire   #Create a database

Records=myDB.Records    #Create a collection

#Insert the record into the collection.
data=[{"name":'sathya','phone':'9999999999','place':'BLR'},
      {"name":'sushma','phone':'8888888888','place':'RNR'},
      {"name":'gokul','phone':'7777777777','place':'MSY'},
      {"name":'subramanian','phone':'6666666666','place':'HOS'},
      {"name":'seetha','phone':'5555555555','place':'KRI'},
      {"name":'sangeetha','phone':'4444444444','place':'BLR'}]

Records.insert_many(data)


#query to find records you just created. 

a=int(input("\n1 to Find by Name \n2 to Find by Phone Number \n3 to Find by Place \n"))

if a==1:
    Name=input("\n")
    query={"name":Name}
    data=Records.find(query)
    for i in data:
       print(i)
elif a==2:
    phone=input("\n")
    query={"phone":phone}
    data=Records.find(query)
    for i in data:
       print(i)
elif a==3:
    place=input("\n")
    query={"place":place}
    data=Records.find(query)
    for i in data:
       print(i)   
       
else:
    print("wrong Input")

#Modify the records, use the update_one() method. The update_one() method requires two arguments, query and update.

b=int(input("\n1 to Mobify by Name \n2 to Mobify by Phone Number \n3 to Mobify by Place \n"))

if b==1:
    Name=input("\n enter the Search Name\n")
    query={"name":Name}
    data=Records.find(query)
    for i in data:
       print(i)
    Input=input("\nenter new Name\n")   
    modify= Records.update_one({"name": Name}, {"$set": {"name":Input}})
    print(modify.matched_count)
    print(modify.modified_count)   
elif b==2:
    Phone=input("\n enter the Search number\n")
    query={"phone":Phone}
    data=Records.find(query)
    for i in data:
       print(i)
    Input=input("\nenter new number\n")
    modify= Records.update_one({"phone":Phone}, {"$set": {"phone":Input}})
    print(modify.matched_count)
    print(modify.modified_count)
elif b==3:
    place=input("\n enter the Search Place\n")
    query={"place":place}
    data=Records.find(query)
    for i in data:
       print(i)
    Input=input("\nenter new place\n")
    modify= Records.update_one({"place":place}, {"$set": {"place":Input}})
    print(modify.matched_count)
    print(modify.modified_count) 
       
else:
    print("wrong Input")

# Delete the record, use delete_one() method. delete_one() requires a query parameter
# which specifies the document to delete.

c=int(input("\n1 to Delete by Name \n2 to Delete by Phone Number \n3 to Delete by Place \n"))

if c==1:
    Name=input("\n enter the  Name\n")
    query={"name":Name}
    data=Records.find(query)
    for i in data:
       print(i)
     
    delet= Records.delete_one({"name": Name})
    print(delet.deleted_count)
   
elif c==2:
    Phone=input("\n enter the number\n")
    query={"phone":Phone}
    data=Records.find(query)
    for i in data:
       print(i)
    delet= Records.delete_one({"phone": Phone})
    print(delet.deleted_count)
elif c==3:
    place=input("\n enter the Place\n")
    query={"place":place}
    data=Records.find(query)
    for i in data:
       print(i)
    delet= Records.delete_one({"place": place})
    print(delet.deleted_count) 
