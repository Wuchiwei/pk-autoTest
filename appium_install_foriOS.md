## 在macOS10.13，使用appium1.7.1版取得app控制元件

 * Install Xcode
 * Install Homebrew
 * Install Appium
 * 使用appium取得app元件
 * 參考資料

##### Install Xcode
1.在終端機輸入以下指令，檢查電腦是否已經存在Xcode
```javascript
    xcodebulid -version
```

2.若尚未安裝，請至[apple官網](https://developer.apple.com/xcode/)下載安裝

3.安裝完成後，請打開xcod～～～～～～檢查模擬氣版本

##### Install Homebrew
1.在終端機輸入以下指令，確認電腦是否已經存在Homebrew
```javascript
    brew -v
```
2.若尚未安裝，在終端機輸入以下指令下載Homebrew
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
1.到[appium官網](http://appium.io/)下載appium

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
3.安裝appium-Python-Client
```javascript
    sudo easy_install pip
```
```javascript
    sudo pip install Appium-Python-Client
```

##### 使用appium取得app元件
1.開啟自官方下載的appium，並點擊start

2.點擊右上角放大鏡輸入資訊已取得app元件名稱

3.輸入資訊如下:

app位置
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

可以從[這裡](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)參考更多能輸入的規格

4.輸入完畢後，點擊右下角Start Session

5.取得元件名稱後，即可開始使用python語法撰寫第一份自動化測試腳本



##### 參考資料
若有其餘相關問題也能參考以下兩個位置資訊

1.youtube[教學影片](https://www.youtube.com/watch?v=IKOXr095jtM)

2.[部落格](https://tracydeng.github.io/2017/02/appium-install/)
