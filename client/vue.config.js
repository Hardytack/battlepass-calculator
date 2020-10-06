// vue.config.js
module.exports = {
  publicPath:
    process.env.NODE_ENV === "production" ? "/battlepass-calculator/" : "",
  css: {
    extract: false,
  },
};
