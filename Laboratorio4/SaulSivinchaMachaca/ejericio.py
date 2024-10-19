def main():
    totalMaleClients = 0
    totalFemaleClients = 0
    totalSalesInRange = 0
    totalFemaleSalesInRange = 0
    totalSalesAmount = 0
    totalType1Amount = 0
    countType1Clients = 0

    while True:
        print("\nMENU OPTIONS")
        print("[1]. REGISTER TICKET SALE")
        print("[2]. SALES REPORT")
        print("[3]. EXIT")
        
        option = int(input("Select an option: "))

        if option == 1:
            clientType = int(input("Enter client type (0-Regular, 1-Special): "))
            ticketCount = int(input("Enter the number of tickets: "))
            clientGender = input("Enter client gender (M-Male, F-Female): ").upper()
            serviceType = int(input("Enter service type (1-Economy, 2-Business, 3-First Class): "))
            
            price = calculatePrice(serviceType)
            if price == 0.0:
                print("Invalid service type.")

            grossAmount = ticketCount * price

            discountAmount = applyDiscount(ticketCount, grossAmount)
            netAmount = grossAmount - discountAmount

            print(f"Gross Amount: ${grossAmount:.2f}")
            print(f"Discount Amount: ${discountAmount:.2f}")
            print(f"Net Amount: ${netAmount:.2f}")

            if clientGender == 'M':
                totalMaleClients += 1
            else:
                totalFemaleClients += 1

            if 70 <= netAmount <= 500:
                totalSalesInRange += 1
            
            if clientGender == 'F' and 140 <= netAmount <= 1000:
                totalFemaleSalesInRange += 1

            totalSalesAmount += netAmount

            if clientType == 1:
                totalType1Amount += netAmount
                countType1Clients += 1

        elif option == 2:
            print("\n--- SALES REPORT ---")
            print(f"Total Male Clients: {totalMaleClients}")
            print(f"Sales between 70 and 500: {totalSalesInRange}")
            print(f"Female Sales between 140 and 1000: {totalFemaleSalesInRange}")
            print(f"Total Sales Amount: ${totalSalesAmount:.2f}")
            print(f"Total Amount for Type 1 Clients: ${totalType1Amount:.2f}")
            if countType1Clients > 0:
                averageType1 = totalType1Amount / countType1Clients
                print(f"Average Amount for Type 1 Clients: ${averageType1:.2f}")
            else:
                print("No Type 1 Clients to calculate the average.")

        elif option == 3:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

def calculatePrice(serviceType):
    if serviceType == 1:
        return 70.0  # Economy
    elif serviceType == 2:
        return 140.0  # Business
    elif serviceType == 3:
        return 280.0  # First Class
    else:
        return 0.0

def applyDiscount(ticketCount, grossAmount):
    if ticketCount == 1:
        discountRate = 0.0
    elif 2 <= ticketCount <= 5:
        discountRate = 0.05
    elif 6 <= ticketCount <= 10:
        discountRate = 0.12
    else:
        discountRate = 0.15
    discountAmount = grossAmount * discountRate
    return discountAmount

if __name__ == "__main__":
    main()
