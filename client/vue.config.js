// vue.config.js
module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/vue-test-2/" : "",
  css: {
    extract: false,
  },
};
