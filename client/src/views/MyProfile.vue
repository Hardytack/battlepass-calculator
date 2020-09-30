<template>
  <section>
    <h1>Hello, {{ username }}</h1>
    <button @click="logout">Sign Out</button>
    <section id="userPasses">
      <h2>You have {{ count }} saved passes</h2>
      <ul class="user-passes">
        <li v-for="pass in passes" :key="pass.id">
          <router-link :to="{ path: `/edit-pass/${pass.id}` }">{{
            pass.bpName
          }}</router-link>
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
      count: 0,
    };
  },
  computed: {
    ...mapGetters(["loggedIn", "username", "token"]),
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
  async created() {
    await fetch("http://127.0.0.1:5000/bp/user-bp?type=all", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${this.token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data.passes);
        if (data.passes.length < 1) {
          return;
        } else {
          this.count = data.passes.length;
          this.passes = data.passes.map((pass) => {
            return { id: pass[0], bpName: pass[2] };
          });
        }
      });
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
