var path = require('path');

module.exports = {
    mode: 'development', // 开发者模式，而productions生产者模式会自动压缩档案

    entry: { // 指定进入点，webpack会以该点开始构建内部以来图
        app: './js/App.js'
    },

    output: { // 告诉webpack创建包的位置和如何命名文件
        path: path.resolve(__dirname, "./dist"), // dist目录通常存放打包或编译过的档案,浏览器可识别
        filename: "scripts.js" // 档案命名
    },

    module: {
        rules: [
            // webpack會將專案內所有的.js檔使用Babel編譯
            {
                test: /\.m?js$/, // 侦测后缀是js的文件
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ['@babel/preset-env', { targets: "defaults"  }]
                        ]
                    }
                }
            }
        ]
    }
};
