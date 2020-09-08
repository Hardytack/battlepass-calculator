<script>
export default {
  name: "Navbar",
  props: {
    title: String,
  },
};
</script>

<template>
  <div id="nav">
    <router-link to="/">Home</router-link>|
    <router-link to="/about">About</router-link>
  </div>
  <!-- <router-view /> -->
</template>

<style lang="scss" scoped>
$red: red;
#navbar {
  h1 {
    color: $red;
  }
}
</style>