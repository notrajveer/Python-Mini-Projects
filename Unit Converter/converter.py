def km_to_miles(km):
    return km*0.621371

def miles_to_km(miles):
    return miles/0.621371

def main():
    print ("1. Kilometeres to Miles")
    print ("2. Miles to Kilometeres")
    
    choice = input("Choose (1/2): ")
    
    try:
        value = float(input("Enter value: "))
        
        if choice == '1':
            print(f"{value} km is {km_to_miles(value):.2f} miles")
        
        elif choice == '2':

            print(f"{value} miles is {miles_to_km(value):.2f} km")
            
    except ValueError:

       print("Enter a valid number.")

if __name__ == "__main__":
    main()