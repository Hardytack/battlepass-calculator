<script>
import { mapGetters } from "vuex";
export default {
  name: "Navbar",
  props: {
    title: String,
  },
  computed: { ...mapGetters(["loggedIn", "username"]) },
};
</script>

<template>
  <div id="nav">
    <router-link to="/">Home</router-link>
    <span> | </span>
    <router-link to="/about">About</router-link>
    <span> | </span>
    <router-link to="/login" v-if="!loggedIn">Login</router-link>
    <router-link to="/my-profile" v-if="loggedIn">{{ username }}</router-link>
  </div>
</template>
