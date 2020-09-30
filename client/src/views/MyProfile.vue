<template>
  <section>
    <h1>Hello, {{ username }}</h1>
    <button @click="logout">Sign Out</button>
    <section id="userPasses">
      <ul>
        <li v-for="pass in passes" :key="pass.id">
          {{ pass.bpName }}
        </li>
      </ul>
    </section>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "MyProfile",
  data() {
    return {
      passes: [],
    };
  },
  computed: {
    ...mapGetters(["loggedIn", "username"]),
  },
  methods: {
    ...mapActions(["signOut"]),
    logout() {
      localStorage.removeItem("username");
      localStorage.removeItem("token");
      this.signOut();
      this.$router.push("/login");
    },
  },
  created() {
    console.log("fetch the stuff");
  },
};
</script>
