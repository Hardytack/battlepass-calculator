<template>
  <section id="signupForm" class="form-container">
    <form @submit.prevent class="form-container">
      <div class="input-group">
        <label>Username</label>
        <input type="text" name="username" v-model.trim="username" />
      </div>
      <div class="input-group">
        <label>Email</label>
        <input type="email" name="email" v-model.trim="email" />
      </div>
      <div class="input-group">
        <label for="user-pass">Password</label>
        <input type="password" name="user-pass" v-model.trim="password" />
      </div>
      <div class="input-group">
        <label for="user-pass">Confirm Password</label>
        <input type="password" name="user-pass" v-model.trim="password2" />
      </div>
      <div class="single-button-group">
        <button @click="signup" :disabled="disableButton">Sign Up</button>
      </div>
      <p class="switchPageLink">
        Already have an Account? <router-link to="/login">Login!</router-link>
      </p>
    </form>
    <p class="errorMessage">{{ errorMessage }}</p>
  </section>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      email: "",
      disableButton: false,
      errorMessage: "",
    };
  },
  methods: {
    ...mapActions(["signIn"]),
    async signup() {
      this.disableButton = true;
      if (!this.username || !this.password || !this.email) {
        this.disableButton = false;
        return (this.errorMessage = "Please fill out all fields");
      }
      if (this.password !== this.password2) {
        this.disableButton = false;
        return (this.errorMessage = "Passwords do not match");
      }
      await fetch(`${process.env.VUE_APP_URL}/auth/register`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          username: this.username.toLowerCase(),
          email: this.email.toLowerCase(),
          password: this.password,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (!data.success) {
            this.disableButton = false;
            this.errorMessage = data.message;
          } else {
            localStorage.setItem("username", data.username);
            localStorage.setItem("token", data.auth_token);
            this.signIn({ username: data.username, token: data.auth_token });
            this.$router.push("/");
          }
        });
    },
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
