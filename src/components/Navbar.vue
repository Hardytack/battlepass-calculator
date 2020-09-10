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
    <router-link to="/">Home</router-link>
    <span> | </span>
    <router-link to="/about">About</router-link>
  </div>
</template>
