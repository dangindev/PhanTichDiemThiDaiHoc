import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv("D:\dangnh4\Documents\PhanTichDiemThiDaiHoc\Data\diem_thi_thpt_2023.csv", sep=",", dtype=str)
df.head()