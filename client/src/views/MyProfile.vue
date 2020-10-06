<template>
  <section>
    <h1>Hello, {{ username }}</h1>
    <button @click="logout">Sign Out</button>
    <section id="userPasses">
      <h2>You have {{ count }} saved passes</h2>
      <table class="user-passes">
        <tbody>
          <tr v-for="pass in passes" :key="pass.id">
            <td>
              <router-link :to="{ path: `/edit-pass/${pass.id}` }">{{
                pass.bpName
              }}</router-link>
            </td>
            <td class="deleteRow">
              <button @click="() => deletePass(pass.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
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
    async deletePass(id) {
      await fetch(`${process.env.VUE_APP_URL}/bp/user-bp?bpid=${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (!data.success) {
            alert(data.message);
          } else {
            this.$router.go(this.$router.currentRoute);
          }
        });
    },
  },
  async created() {
    await fetch(`${process.env.VUE_APP_URL}/bp/user-bp?type=all`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${this.token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
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
