# 台股兵法智謀全媒體觀測系統 - Streamlit 完整專案版

這是依照你提供的 React/TypeScript 程式封裝出的 Streamlit 可部署版本。

## 檔案內容
- `app.py`：Streamlit 主程式
- `index.html`：可嵌入的前端單頁
- `requirements.txt`：Python 套件需求
- `source_reference.ts`：你原始上傳的程式碼備份
- `README.md`：部署說明

## 本機測試
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit Community Cloud
1. 建立 GitHub Repository
2. 把本資料夾全部檔案上傳到 Repository 根目錄
3. 到 Streamlit Community Cloud
4. 點 `Create app`
5. Repository 選你的 GitHub 專案
6. Branch 選 `main`
7. Main file path 填 `app.py`
8. 按 `Deploy`

## 注意
- `index.html` 與 `app.py` 必須在同一層
- 此頁面使用外部 CDN 載入 React、Tailwind 與 Babel
- 需網路連線才能正常顯示
