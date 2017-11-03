## 在 macOS10.13，使用 appium1.7.1 版取得 app 控制元件

 * Install Xcode
 * Install Homebrew
 * Install Appium
 * 使用 appium 取得 app 元件
 * 參考資料

##### 在 macOS10.13 環境

![avatar](https://i.imgur.com/xkygLQN.png)

##### Install Xcode
1.在終端機輸入以下指令，檢查電腦是否已經存在 Xcode
```javascript
    xcodebulid -version
```

![avatar](https://i.imgur.com/Yu8ddRo.png)

2.安裝完成後，請打開 xcode 找到模擬器版本

STEP1. 開啟 xcode 第一份專案並確認模擬器可以成功開啟

![avatar](https://i.imgur.com/VPIlswI.png)

![avatar](https://i.imgur.com/TNtVWA9.png)

STEP2.尋找模擬器其他可用版本，後續設定 appium 參數時會使用到

Xcode -> Preferences ，表單出現後點擊上方工具列的 Components 即可看到其他可用版本

![avatar](https://i.imgur.com/mvGEqsG.png)

3.若尚未安裝，請至 [apple 官網](https://developer.apple.com/xcode/)下載安裝

![avatar](https://i.imgur.com/8BNRuQM.png)

##### Install Homebrew
1.在終端機輸入以下指令，確認電腦是否已經存在 Homebrew
```javascript
    brew -v
```
![avatar](https://i.imgur.com/Ql7mwrn.png)

2.若尚未安裝，在終端機輸入以下指令下載 Homebrew
```javascript
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


3.在終端機中分別輸入以下兩個指令更新Homebrew
```javascript
    brew update
```
```javascript
    brew install carthage
```
##### Install Appium
1.到 [appium 官網](http://appium.io/)下載appium

2.安裝完成後，在終端機分別輸入以下指令
```javascript
    brew install node
```
```javascript
    npm install -g appium
```
```javascript
    npm install wd
```
3.安裝 appium - Python - Client
```javascript
    sudo easy_install pip
```
```javascript
    sudo pip install Appium-Python-Client
```

##### 使用 appium 取得 app 元件
1.開啟自官方下載的 appium，並點擊 start

![avatar](https://i.imgur.com/nobxzix.png)

2.點擊右上角放大鏡輸入資訊已取得 app 元件名稱

![avatar](https://i.imgur.com/KJGClSm.png)

3.輸入資訊如下:

app 位置
```javascript
    "app": 檔案路徑
```
版本（必須輸入模擬器裡面具有的版本才能使用）
```javascript
    "platformVersion": "11.0"
```
平台名稱
```javascript
   "platformName": "iOS"
```
手機型號
```javascript
   "deviceName": "iPhone 6"
```

![avatar](https://i.imgur.com/scY3UuY.png)

可以從[這裡](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)參考更多能輸入的規格

4.輸入完畢後，點擊右下角 Start Session

![avatar](https://i.imgur.com/v5STwkB.png)

5.取得元件名稱後，即可開始使用 python 語法撰寫第一份自動化測試腳本



##### 參考資料
若有其餘相關問題也能參考以下兩個位置資訊

1.youtube [教學影片](https://www.youtube.com/watch?v=IKOXr095jtM)

2.[部落格](https://tracydeng.github.io/2017/02/appium-install/)
