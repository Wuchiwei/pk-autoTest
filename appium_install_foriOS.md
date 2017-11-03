# 在 macOS 10.13 ，使用 appium 1.7.1 版取得  iOS app 元件名稱

這篇文章主要是針對在 macOS 10.13 環境下，使用 appium 官方網站的自動化測試套件來取得需要測試的 iOS app 元件名稱，
//TODO: 你的文章內容沒寫到 python 語法，是漏寫了，還是這段打錯了？
最後結合 python 語法來撰寫自動化測試腳本。


 接著會依照以下幾個步驟來架設好 appium 的環境

 1. Install Xcode
 2. Install Homebrew
 3. Install Appium
 4. 使用 appium 取得 iOS app 元件
 5. 參考資料

### 確認在 macOS 10.13 環境底下

![avatar](https://i.imgur.com/xkygLQN.png)

### Install Xcode

自動腳本的測試可以在 iOS 模擬器，也可以直接在實體機上面執行。

這邊選擇在 iOS 模擬器上執行，使用 Xcode 所提供的 simulator 來執行動作。

##### 1. 在終端機輸入以下指令，檢查電腦是否已經存在 Xcode
//TODO: 為什麼 需要加上 javascript，還有這行指令有機會會失敗，建議請使用者在 app store 搜尋 xcode 的方式來確認
```javascript
    xcodebulid -version
```

![avatar](https://i.imgur.com/Yu8ddRo.png)

##### 2. 若尚未安裝，請至 App Store 搜尋 Xcode 並下載


##### 3. 安裝完成後，打開 xcode 找到模擬器版本

* STEP 1. 開啟 xcode 第一份專案並確認模擬器可以成功開啟

![avatar](https://i.imgur.com/VPIlswI.png)

![avatar](https://i.imgur.com/TNtVWA9.png)

* STEP 2. 尋找模擬器其他可用版本，後續設定 appium 參數時會使用到

在 Xcode -> Preferences ，表單出現後點擊上方工具列的 Components 即可看到其他可用版本

![avatar](https://i.imgur.com/mvGEqsG.png)

### Install Homebrew

這個是方便用來管理 Mac 中的套件下載以及卸載的工具，後面會用這個工具來下載相關的套件。

//TODO: 為什麼 需要加上 javascript
* 1. 在終端機輸入以下指令，先確認電腦是否已經存在 Homebrew
```javascript
    brew -v
```
![avatar](https://i.imgur.com/Ql7mwrn.png)

* 2. 若尚未安裝，在終端機輸入以下指令下載 Homebrew
//TODO: 為什麼 需要加上 javascript
```javascript
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* 3. 在終端機中分別輸入以下兩個指令更新 Homebrew
//TODO: 為什麼 需要加上 javascript
```javascript
    brew update
```
//TODO: 為什麼 需要加上 javascript
```javascript
    brew install carthage
```
### Install Appium

前置作業完成後，現在可以開始下載 appium ，以及下載後續會使用 python 語法來撰寫腳本的 appium - Python - Client 資源。

##### 1. 到 [appium 官網](http://appium.io/)下載 appium

![avatar](https://i.imgur.com/8BNRuQM.png)

##### 2. 安裝完成後，在終端機分別輸入以下指令
//TODO: 為什麼 需要加上 javascript
```javascript
    brew install node
```
//TODO: 為什麼 需要加上 javascript
```javascript
    npm install -g appium
```
//TODO: 為什麼 需要加上 javascript
```javascript
    npm install wd
```
//TODO: 這次有需要裝 Python 嗎？
##### 3. 安裝 appium - Python - Client
//TODO: 為什麼 需要加上 javascript
```javascript
    sudo easy_install pip
```
//TODO: 為什麼 需要加上 javascript
```javascript
    sudo pip install Appium-Python-Client
```

### 使用 appium 取得 iOS app 元件

到這裡可以開始使用 appium 來取得 iOS app 的元件

1. 開啟自官方下載的 appium，並點擊 start

![avatar](https://i.imgur.com/nobxzix.png)

2. 點擊右上角放大鏡輸入資訊已取得 iOS app 元件名稱

![avatar](https://i.imgur.com/KJGClSm.png)

3. 輸入資訊如下:

iOS app 位置
//TODO: 為什麼 需要加上 javascript
```javascript
    "app": 檔案路徑
```
版本（必須輸入模擬器裡面具有的版本才能使用）
//TODO: 為什麼 需要加上 javascript
```javascript
    "platformVersion": "11.0"
```
平台名稱
//TODO: 為什麼 需要加上 javascript
```javascript
   "platformName": "iOS"
```
手機型號
//TODO: 為什麼 需要加上 javascript
```javascript
   "deviceName": "iPhone 6"
```

![avatar](https://i.imgur.com/scY3UuY.png)

可以從[這裡](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)參考更多能輸入的規格

4. 輸入完畢後，點擊右下角 Start Session

![avatar](https://i.imgur.com/v5STwkB.png)

5. 取得元件名稱後，即可開始撰寫第一份自動化測試腳本。




##### 參考資料
若有其餘相關問題也能參考以下兩個位置資訊

1.youtube [教學影片](https://www.youtube.com/watch?v=IKOXr095jtM)

2.[部落格](https://tracydeng.github.io/2017/02/appium-install/)
