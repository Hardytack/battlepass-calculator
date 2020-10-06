<template>
  <section id="loginForm" class="form-container">
    <form @submit.prevent>
      <div class="input-group">
        <label>Username</label>
        <input type="text" name="username" v-model.trim="username" />
      </div>
      <div class="input-group">
        <label for="user-pass">Password</label>
        <input type="password" name="user-pass" v-model.trim="password" />
      </div>
      <div class="single-button-group">
        <button @click="login" :disabled="disableButton">Login</button>
      </div>
      <p class="switchPageLink">
        Don't have an Account? <router-link to="/signup">Sign Up!</router-link>
      </p>
    </form>
    <p class="errorMessage">{{ errorMessage }}</p>
  </section>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      disableButton: false,
      errorMessage: "",
    };
  },
  methods: {
    ...mapActions(["signIn"]),
    async login() {
      if (!this.username || !this.password) {
        return (this.errorMessage = "Please fill out all fields");
      }
      // this.disableButton = true;
      await fetch(`${process.env.VUE_APP_URL}/auth/login`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          if (!data.success) {
            this.disableButton = false;
            this.errorMessage = data.message;
          } else {
            localStorage.setItem("token", data.auth_token);
            localStorage.setItem("username", data.username);
            this.signIn({ username: data.username, token: data.auth_token });
            this.$router.push({ path: "/" });
          }
        });
    },
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
