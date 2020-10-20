var webpack = require('webpack');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: 'production',
    plugins: [
        new webpack.DefinePlugin({
            'process.env':{
                'API_URL': JSON.stringify('http://ec2-18-208-169-230.compute-1.amazonaws.com')
            }
        }),
    ]
});
