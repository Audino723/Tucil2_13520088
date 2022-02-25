import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import ConvexHullRio

def convex_hull(bucket):
    return ConvexHullRio.main(bucket)
    
def visualize(df, data, features):
    #visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    plt.title(f'{data.feature_names[features[0]]} vs {data.feature_names[features[1]]}')
    plt.xlabel(data.feature_names[features[0]])
    plt.ylabel(data.feature_names[features[1]])
    
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[features[0],features[1]]].values
        hull = convex_hull(bucket)
        color = (np.random.random(), np.random.random(),np.random.random())
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=color)
        for data_points in hull:
            plt.plot(data_points[0], data_points[1], color=color)

    plt.legend()
    plt.show()

def choose_feature(data):
    choosed_feature = [0,0]
    while True:
        print("Choose two feature: ")
        for i, name in enumerate(data.feature_names):
            print(f"{i+1}.", name)
        choosed_feature[0] = (int(input("Feature-x : "))-1)
        choosed_feature[1] = (int(input("Feature-y : "))-1)

        if (choosed_feature[0] == choosed_feature[1] or 
        not(0<=choosed_feature[0]<len(data.feature_names)) or
        not(0<=choosed_feature[1]<len(data.feature_names))):
            print("Input not valid")
        else:
            break

        print()

    return choosed_feature

def main():
    # CHOOSE DATASET
    data = datasets.load_wine()

    # Converting to pandas dataframe
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    # Choosing features & Visualization
    choosed_feature = choose_feature(data)
    visualize(df, data, choosed_feature)

if __name__ == "__main__":
    main()