import pandas
from pathlib import Path

df = pandas.read_csv('day8_tasks/data.csv')

print(df)

# # 相对路径写法
# base_dir = Path(__file__).parent
# csv_path = base_dir / "data.csv"
#
# df = pd.read_csv(csv_path)
# print(df)

# longitude,latitude,housing_median_age,total_rooms,total_bedrooms,
# population,households,median_income,median_house_value,ocean_proximity

# 清洗数据
# 1. 缺失数据 -> 中位数补充
cols = ["total_rooms","total_bedrooms","population","households","median_income","median_house_value"]
df[cols] = df[cols].fillna(df[cols].median())

# 2. 值被封顶(标记)
df["median_house_value_is_value_capped"] = (df["median_house_value"] >= 500000)

# 存储
out_dir = Path('day8_tasks')
out_dir.mkdir(exist_ok=True)

df.to_csv('day8_tasks/housing_cleaned.csv', index=False)




