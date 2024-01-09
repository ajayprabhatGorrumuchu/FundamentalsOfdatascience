import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#File name
data_file = "data0-1.csv"

def loadData(filename , columnName):
    """
        Load data from a CSV file into a pandas DataFrame.

        Parameters:
        - filename (str): The name of the CSV file to load.
        - columnName (str): The desired name for the column in
        the DataFrame.

        Returns:
        - pd.DataFrame: A DataFrame containing the loaded data
        with the specified column name.
    """
    data = pd.read_csv(filename , header = None , names = [columnName])
    return data


def pdfCurve(data , mean , xvalue):
    """
        Plot a probability density function (PDF) curve along
        with a histogram and key statistics.

        Parameters:
        - data (array-like): The dataset to be plotted.
        - mean (float): The mean value of the dataset.
        - xvalue (float): The specified value X.

        Returns:
        None
    """

    # Create a probability density function and plot it as a histogram
    n , bins , _ = plt.hist(data , bins = 30 , density = True , alpha = 0.5 ,
                          color = "Brown" , label = "Sample Data")

    # Fit a normal distribution to the data
    mu , std = np.mean(data) , np.std(salaries["Salary"])

    # Plot the PDF curve
    xmin , xmax = plt.xlim()
    x = np.linspace(xmin , xmax , 100)
    p = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)
                                                   ** 2 / (2 * std ** 2))
    plt.plot(x , p , 'k' , linewidth = 2 , label = "Fitted PDF")

    # Add mean and X values to the graph
    plt.axvline(mean , color = "r" , linestyle = "dashed" , linewidth = 2 ,
                label = "Mean Salary=" + str(mean))
    plt.axvline(xvalue , color = "g" , linestyle = "dashed" , linewidth = 2 ,
                label = "X=" + str(xvalue))

    # Set labels, title, and legend
    plt.xlabel("Annual Salary (Euros)" , fontweight='bold')
    plt.ylabel("Probability Density" , fontweight='bold')
    plt.title("Probability Density Function of Salaries" , fontweight='bold')
    plt.legend()

    # Show the graph
    plt.show()


#load data
salaries = loadData(data_file , "Salary")

# Calculate the mean annual salary and x value
mean_salary = np.mean(salaries["Salary"]).round(2)
print("mean salay = "+str(mean_salary)+' euros')
X = np.percentile(salaries["Salary"] , 75).round(2)
print('x value(75th percentile) = '+str(X))

pdfCurve(salaries["Salary"] , mean_salary , X)





