const BundleTracker = require("webpack-bundle-tracker");

const webpackConfig = config => {
  config.optimization.splitChunks(false)

  config.resolve.alias.set('__STATIC__', 'static')

  config.devServer
    .public('http://0.0.0.0:8080')
    .host('0.0.0.0')
    .port(8080)
    .hotOnly(true)
    .watchOptions({poll: 1000})
    .https(false)
    .headers({"Access-Control-Allow-Origin": ["\*"]})

  config.plugin('BundleTracker')
    .use(BundleTracker, [{filename: 'webpack-stats.json'}])
}

module.exports = {
  publicPath: 'http://0.0.0.0:8080',
  outputDir: './dist/',
  chainWebpack: webpackConfig,
}

