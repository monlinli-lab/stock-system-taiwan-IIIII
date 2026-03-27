# 台股兵法智謀全媒體觀測系統 - Streamlit 上傳版

這是可直接上傳到 GitHub 並部署到 Streamlit Community Cloud 的版本。

## 專案檔案
- `app.py`：Streamlit 主程式
- `index.html`：前端展示頁面
- `requirements.txt`：套件需求
- `README.md`：部署說明

## 本機執行
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit Community Cloud
1. 建立 GitHub Repository
2. 將本資料夾內全部檔案上傳到 Repository 根目錄
3. 到 Streamlit Community Cloud
4. 點選 `Create app`
5. Repository 選你的 GitHub 專案
6. Branch 選 `main`
7. Main file path 填 `app.py`
8. 點 `Deploy`

## 注意
- `index.html` 與 `app.py` 必須在同一層
- 本頁使用外部 CDN 載入部分前端資源，部署時需要網路連線
