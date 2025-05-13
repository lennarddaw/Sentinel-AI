import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

class PoisonDetector:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.model = IsolationForest(contamination=0.05)

    def run(self):
        print(f"Running outlier detection on {self.data.shape[0]} rows...")
        features = self.data.select_dtypes(include=['number']).dropna()
        preds = self.model.fit_predict(features)
        self.data["outlier"] = preds
        return self.data

    def plot(self, x, y):
        sns.scatterplot(data=result, x="feature1", y="feature2", hue="outlier", palette="coolwarm")
        plt.title("Outlier Detection Result")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()
