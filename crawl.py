import requests
import time
import pandas as pd
import os

cities = {"S\u1edf GD\u0110T H\u00e0 N\u1ed9i": "01000001", "S\u1edf GD\u0110T TP. H\u1ed3 Ch\u00ed Minh": "02000001", "S\u1edf GD\u0110T H\u1ea3i Ph\u00f2ng": "03000001", "S\u1edf GD\u0110T \u0110\u00e0 N\u1eb5ng": "04000001", "S\u1edf GD\u0110T H\u00e0 Giang": "05000001", "S\u1edf GD\u0110T Cao B\u1eb1ng": "06000001", "S\u1edf GD\u0110T Lai Ch\u00e2u": "07000001", "S\u1edf GD\u0110T L\u00e0o Cai": "08000001", "S\u1edf GD\u0110T Tuy\u00ean Quang": "09000001", "S\u1edf GD\u0110T L\u1ea1ng S\u01a1n": "10000001", "S\u1edf GD\u0110T B\u1eafc K\u1ea1n": "11000001", "S\u1edf GD\u0110T Th\u00e1i Nguy\u00ean": "12000001", "S\u1edf GD\u0110T Y\u00ean B\u00e1i": "13000001", "S\u1edf GD\u0110T S\u01a1n La": "14000001", "S\u1edf GD\u0110T Ph\u00fa Th\u1ecd": "15000001", "S\u1edf GD\u0110T V\u0129nh Ph\u00fac": "16000001", "S\u1edf GD\u0110T Qu\u1ea3ng Ninh": "17000001", "S\u1edf GD\u0110T B\u1eafc Giang": "18000001", "S\u1edf GD\u0110T B\u1eafc Ninh": "19000001", "S\u1edf GD\u0110T H\u1ea3i D\u01b0\u01a1ng": "21000001", "S\u1edf GD\u0110T H\u01b0ng Y\u00ean": "22000001", "S\u1edf GD\u0110T Ho\u00e0 B\u00ecnh": "23000001", "S\u1edf GD\u0110T H\u00e0 Nam": "24000001", "S\u1edf GD\u0110T Nam \u0110\u1ecbnh": "25000001", "S\u1edf GD\u0110T Th\u00e1i B\u00ecnh": "26000001", "S\u1edf GD\u0110T Ninh B\u00ecnh": "27000001", "S\u1edf GD\u0110T Thanh Ho\u00e1": "28000001", "S\u1edf GD\u0110T Ngh\u1ec7 An": "29000001", "S\u1edf GD\u0110T H\u00e0 T\u0129nh": "30000001", "S\u1edf GD\u0110T Qu\u1ea3ng B\u00ecnh": "31000001", "S\u1edf GD\u0110T Qu\u1ea3ng Tr\u1ecb": "32000001", "S\u1edf GD\u0110T Th\u1eeba Thi\u00ean -Hu\u1ebf": "33000001", "S\u1edf GD\u0110T Qu\u1ea3ng Nam": "34000001", "S\u1edf GD\u0110T Qu\u1ea3ng Ng\u00e3i": "35000001", "S\u1edf GD\u0110T Kon Tum": "36000001", "S\u1edf GD\u0110T B\u00ecnh \u0110\u1ecbnh": "37000001", "S\u1edf GD\u0110T Gia Lai": "38000001", "S\u1edf GD\u0110T Ph\u00fa Y\u00ean": "39000001", "S\u1edf GD\u0110T \u0110\u1eafk L\u1eafk": "40000001", "S\u1edf GD\u0110T Kh\u00e1nh Ho\u00e0": "41000001", "S\u1edf GD\u0110T L\u00e2m \u0110\u1ed3ng": "42000001", "S\u1edf GD\u0110T B\u00ecnh Ph\u01b0\u1edbc": "43000001", "S\u1edf GD\u0110T B\u00ecnh D\u01b0\u01a1ng": "44000001", "S\u1edf GD\u0110T Ninh Thu\u1eadn": "45000001", "S\u1edf GD\u0110T T\u00e2y Ninh": "46000001", "S\u1edf GD\u0110T B\u00ecnh Thu\u1eadn": "47000001", "S\u1edf GD\u0110T \u0110\u1ed3ng Nai": "48000001", "S\u1edf GD\u0110T Long An": "49000001", "S\u1edf GD\u0110T \u0110\u1ed3ng Th\u00e1p": "50000001", "S\u1edf GD\u0110T An Giang": "51000001", "S\u1edf GD\u0110T B\u00e0 R\u1ecba-V\u0169ng T\u00e0u": "52000001", "S\u1edf GD\u0110T Ti\u1ec1n Giang": "53000001", "S\u1edf GD\u0110T Ki\u00ean Giang": "54000001", "S\u1edf GD\u0110T C\u1ea7n Th\u01a1": "55000001", "S\u1edf GD\u0110T B\u1ebfn Tre": "56000001", "S\u1edf GD\u0110T V\u0129nh Long": "57000001", "S\u1edf GD\u0110T Tr\u00e0 Vinh": "58000001", "S\u1edf GD\u0110T S\u00f3c Tr\u0103ng": "59000001", "S\u1edf GD\u0110T B\u1ea1c Li\u00eau": "60000001", "S\u1edf GD\u0110T C\u00e0 Mau": "61000001", "S\u1edf GD\u0110T \u0110i\u1ec7n Bi\u00ean": "62000001", "S\u1edf GD\u0110T \u0110\u0103k N\u00f4ng": "63000001", "S\u1edf GD\u0110T H\u1eadu Giang": "64000001"}

# Tạo DataFrame rỗng
df = pd.DataFrame()


# Kiểm tra file CSV
file_exists = os.path.isfile('data.csv')

for city, start_code in cities.items():
    code = int(start_code)
    print(code)
    while True:
        url = f"https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={str(code).zfill(8)}&nam=2023"
        try:
            response = requests.get(url)
            data = response.json()

            if not data or 'error' in data:
                break

            flat_data = pd.json_normalize(data['result'])
            
            # Bỏ cột CityArea
            flat_data = flat_data.drop('CityArea', axis=1)

            # Lấy header từ DataFrame đầu tiên nếu file chưa tồn tại
            if not file_exists and not flat_data.empty:
                header = flat_data.columns.tolist()
                flat_data.to_csv('./Data/data.csv', mode='w', header=header, index=False)  # Ghi với mode='w' để ghi đè
                file_exists = True
            else:
                # Ghi dữ liệu vào file CSV (không có header)
                flat_data.to_csv('./Data/data.csv', mode='a', header=False, index=False)

            print(flat_data)
            code += 1
            time.sleep(0.1)

        except:
            break