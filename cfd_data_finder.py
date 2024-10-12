import pandas as pd

# Function to load CFD data from a CSV file
def load_cfd_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CFD data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to find CFD data for a specific F1 car
def find_cfd_data(data, car_name):
    # Filter the data for the specified car name
    result = data[data['Car_Name'].str.contains(car_name, case=False, na=False)]
    
    if result.empty:
        print(f"No CFD data found for the car: {car_name}")
    else:
        print("CFD Data for car:", car_name)
        print(result)

# Main function to run the program
def main():
    # Path to the CFD data file
    file_path = "f1_cfd_data.csv"  # Change this to your CSV file path
    
    # Load CFD data
    cfd_data = load_cfd_data(file_path)
    
    if cfd_data is not None:
        # Get car name input from user
        car_name = input("Enter the name of the F1 car you want to find CFD data for: ")
        
        # Find and display CFD data for the specified car
        find_cfd_data(cfd_data, car_name)

if __name__ == "__main__":
    main()
