import os
from poison_detector.detector import PoisonDetector

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "train.csv")

detector = PoisonDetector(csv_path)


result = detector.run()

print(result.head())

detector.plot(x="feature1", y="feature2")
