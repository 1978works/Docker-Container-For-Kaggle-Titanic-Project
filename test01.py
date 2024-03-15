import pandas as pd
import os
os.chdir("/workspace/.devcontainer/")
devcontainer_dir: str = os.getcwd()
dataset_dir: str = devcontainer_dir+"/dataset"


# datasetディレクトリ直下のcsvファイルをすべて読み込む
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
                
csv_files: list[str] = get_csv(dataset_dir)
titanic_test_csv = pd.read_csv(dataset_dir+"/"+csv_files[1])
titanic_test_csv
        
        
        
    