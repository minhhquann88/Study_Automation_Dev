from pathlib import Path

import pandas as pd


def merge_csvg(folder_path):
    path_dir = Path(folder_path)
    csv_files = list(path_dir.glob('*.csv'))
    # Tạo list chứa các DataFrame nhỏ

    df_list = []
    for f in csv_files:
        df = pd.read_csv(f)
        # Sửa tên tất cả các cột thành chữ thường TRƯỚC KHI cho vào list
        df.columns = df.columns.str.lower()
        df_list.append(df)

    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df = merged_df.drop_duplicates()
    merged_df.to_csv('merged.csv', index=False)

merge_csvg('Phase 1/Week 2/data')
