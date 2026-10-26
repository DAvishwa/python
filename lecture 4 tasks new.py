for number in range (1,51):
   print  (number)

   for number in range (2,101,2):
      print (number)  

      student = {
         "name":"rohan",
         "age": 23,
         "percentage" : 90,
         "is_pass" : "true"

      }
      print (student)




cites = ["goa","ahmedabad","nepal","mumbai"]
cites.remove('goa')
print(cites)

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Delhi"
}
print(student["name"],student["city"])   

price = 100
print(int(price))


x = 10
print(float(x))


number = 50
text = str(number)
print(text)


total = 0
for i in range(1,101):
       total+=i
       print("total:",total)
       
       sales = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
       total = 0
       for value in sales:
              total +=value
              average=total/len(sales)
              print("total sales:",total)
              print("average sales:",average)
              
sales =[25000,60000,75000,40000,90000,55000]
count = 0
for value in sales:
       if value > 50000:
              count +=1
              print("sales above 50000:",count)
              
sales =[25000,60000,75000,40000,90000]
highest = sales[0]
for value in sales:
   if value >highest:             
              highest = value
              print("highest sales:",highest)
sales =[25000,40000,75000,900000,60000]
lowest = sales[0]
for value in sales:
   if value < lowest:
      lowest = value
      print("lowest sales:",lowest)
transactions =[1000,-500,2000,-300,1500,-100]
count = 0
for value in transactions:
   if value < 0:
      count +=1
      print("negative transactions:",count)
      
sales =[50000,60000,70000]
cost =[30000,40000,45000]
for i in range(len(sales)):
   profit = sales[i] - cost[i]
   print("product",i +1,"profit:",profit)
               
                    
marks =[25,45,60,30,80,70]
count = 0
for mark in marks:
   if mark>=35:
      count +=1
      print("students passed:",count)
      
customers =["rahul","","priya","amit","","neha"]
for name in customers:
   if name!="":
      print(name)
      
i = 10
while i>=1:
   print(i)
   i-=1
         
sales =[25000,50000,75000,12000,60000,150000]
for value in sales:
   if value>100000:
      print("value found:",value)
      print("processing:",value)
                  
                    
quantites =[10,20,25,15,5]
prices =[100,200,300,400,150]
total_revenue = 0
for i in range(len(quantites)):
       total_revenue += quantites[i]* prices[i]
       print("total revenue:",total_revenue)
       




      