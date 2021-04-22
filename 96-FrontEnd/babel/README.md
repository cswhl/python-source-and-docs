- 创建webpack环境
1.初始化,创建package.json: npm init -y
2.安裝webpack套件：npm -i -D webpack webpack-cli
3.配置webpack的打包规则: webpack.config.js
4.webpack使用配置文件指导编译和打包:npx webpack --config webpack.config.js
5、用npm來安裝babel相关的module和loader:
npm install -D babel-loader @babel/core @babel/preset-env webpack
6、安装第三方js lib : npm install jquery]


执行编译: npm run build, 编译合打包js

- 验证babel能否正常运行
python3 -m http.server 9999：创建一个简单服务器，可以从chrome 浏览器访问网页
浏览器控制台输出正常说明babel配置ok
