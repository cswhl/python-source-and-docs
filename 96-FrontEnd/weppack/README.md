- 创建webpack环境
1.初始化,创建package.json: npm init -y
2.安裝webpack套件：npm -i -D webpack webpack-cli
3.配置webpack的打包规则: webpack.config.js
4.webpack使用配置文件指导编译和打包:npx webpack --config webpack.config.js

- 验证webpack能否正常运行

python3 -m http.server 9999：创建一个简单服务器，可以从chrome 浏览器访问网页
浏览器控制台输出正常说明webpack配置ok
