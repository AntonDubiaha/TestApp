const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: './frontend/src/index.js',
  module: {
    rules: [{ 
        test: /\.(js)$/, 
        exclude: /node_modules/,
        use: 'babel-loader' 
    }]
  },
  output: {
    path: path.resolve(__dirname, './frontend/static/frontend'),
    filename: 'main.js'
  },
  plugins: [
    new HtmlWebpackPlugin()
  ],
  mode: 'development'
}