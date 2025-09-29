import yaml

with open('simple.yaml', 'r') as file:
    details = yaml.safe_load(file)
print ("Full yaml content:", details)

for emp in details['Employees']:
    print ("Employee Name:", emp['name'])
    print ("Employee Age:", emp['age'])
    print ("Married:", emp['married'])
    print ("Employee Skills:", ", ".join(emp['skills']))
    print ("---")