<template>
  <div id="app">
    <div class="imageContainer">
      <img alt="Battlepass Calculator" src="./assets/bp-logo.png" />
    </div>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import { mapActions } from "vuex";
export default {
  name: "App",
  components: {
    Navbar,
  },
  methods: {
    ...mapActions(["signIn"]),
    handleEmit(e) {
      console.log(e);
    },
  },
  created() {
    console.log(process.env.VUE_APP_URL);
    if (localStorage.getItem("username") && localStorage.getItem("token")) {
      this.signIn({
        username: localStorage.getItem("username"),
        token: localStorage.getItem("token"),
      });
    }
  },
};
</script>

//
<style lang="scss">
$lightGreen: #f1ffe6;
* {
  box-sizing: border-box;
}
html {
  width: 100%;
}
body {
  background-color: #333;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #f1ffe6;
  width: 100%;
}

#nav {
  padding: 10px 30px 15px 30px;
}

#nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: #bada55;
}

.imageContainer {
  width: 90%;
  margin: 0 auto;
  overflow: hidden;
  max-width: 500px;
  img {
    width: 100%;
    display: block;
  }
}
</style>
