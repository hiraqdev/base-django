var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require("extract-text-webpack-plugin");

function resolve(dir) {
    return path.join(__dirname, '..', dir)
}

module.exports = {
    context: __dirname,

    entry: {
        index: './assets/js/index',
        bootstrap: './assets/js/bootstrap'
    },

    output: {
        path: path.resolve('./assets/bundles/'),
        filename: "[name]-[hash].js",
    },

    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new ExtractTextPlugin({
            filename: 'style.css',
            allChunks: true,
            ignoreOrder: true,
        }),
    ],

    performance: {
        hints: false,
    },

    stats: { colors: true },

    optimization: {
        splitChunks: {
            name: 'common'
        }
    },

    resolve: {
        extensions: ['.js', '.vue', '.json'],
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
        },
    },

    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                include: [resolve('src'), resolve('test')]
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: ['css-loader']
                })
            }
        ]
    }
}
