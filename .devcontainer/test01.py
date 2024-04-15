import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
os.chdir("/workspace/.devcontainer/")
devcontainer_dir: str = os.getcwd()
dataset_dir: str = devcontainer_dir+"/dataset"


# datasetディレクトリ直下のcsv「ファイル名」を取得
def get_csv(path: str) -> list[str]:
    """CSVファイルだけのファイル名をリストにする関数

    Args:
        path (str): CSVファイルがディレクトリへのパス

    Returns:
        list[str]:CSVファイルだけのファイル名のリスト
    """
    
        
    temp_result: list[str] = os.listdir(path)
    if temp_result == []:
        print("ファイルがありません")
    else:
        csv_files: list = []
        for i in temp_result:
            if i.endswith("csv"):
                csv_files.append(i)
    return csv_files
                
# csvの名前をリスト化
csv_files: list[str] = get_csv(dataset_dir)
# 各csvを読み込み、データフレームオブジェクト化

test_df = pd.read_csv(dataset_dir+"/"+csv_files[0])
train_df = pd.read_csv(dataset_dir+"/"+csv_files[1])
sub_df = pd.read_csv(dataset_dir+"/"+csv_files[2])

# ydata_profilingの使用
profile = ProfileReport(train_df, title="Profiling Report")
#Jupyternotebook以外での使用法
dir(profile)

profile.to_file("titanic_report.html")



# DFの行数・列数の確認
print(train_df.shape)
#DFのインデックス確認
index_range = train_df.index
for i in index_range[880:885]:
    print(i)

# 列の名前の確認
print(train_df.columns)
print('='*40)  # 区切り線を描写
print(train_df.columns)

# DFの列ごとの型などの概要確認
print(train_df.info())

# DFの先頭10行だけ表示
print(train_df.head(5))

# 欠損値の確認
print(train_df.isnull())
print(train_df.isnull().sum()) 

# 各列の要約統計量(count: 数値データの数）
print(train_df.describe())

# top: the most common value
# freq: the most common value’s frequency.
train_df.describe(include=['O'])

# 20%ずつ表示（つまり、５分割
print(train_df.describe(percentiles=[.2, .4, .6, .8,]))

# 平均、中央値、標準偏差
print(train_df.mean)x
print(train_df.median)
print(train_df.std)

# 列Ageだけ抽出
train_df['Age']
type(train_df['Age'])

# 列Ageと列Survivedを抽出
train_df.loc[:, ['Age', 'Survived']]

# 上と同じ
train_df[['Age', 'Survived']]
type(train_df[['Age', 'Survived']])


# 列Ageと列Survivedを抽出し、列Ageを基準にソート
train_df.loc[:, ['Age', 'Survived']].sort_values('Age')


# 列Ageと列Survivedを抽出し、列Ageを基準にソートして、NaNをもつセルを削除
train_df.loc[:, ['Age', 'Survived']].sort_values('Age').dropna()

# ピアソン相関係数
train_df[["Age", "Survived"]].dropna().sort_values("Age").corr('pearson')




