n = int(input("Number of streams"))
flows = [int(input()) for i in range(n)]

flow_input = 0

while flow_input != 77:
    flow_input = int(input("Enter the flow number: "))

    if flow_input == 99:
        flow_int = int(input("Enter the number that is split: "))
        flow_pct = int(input("Enter the percentage of the flow: "))
        
        
    if flow_input == 88:
        flow_int = int(input("Enter the number that is merged: "))
        
print 