import requests
import json

# 设置请求的URL和Headers
url = "https://192.168.0.10:30061/trailv2/api/case/page"  # 替换为实际接口URL
params = {
"state": "All",
"pageSize": 10,
"pageNum": 1,
}
headers = {
    "x-token":"b403ec2f-2a35-47ec-b211-5b030848af02",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

def fetch_data():
    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()  # 获取JSON格式的数据
        return data
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def main():
    data = fetch_data()
    if data:
        # 处理数据，例如保存到文件
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("数据已保存到data.json")

if __name__ == "__main__":
    main()
