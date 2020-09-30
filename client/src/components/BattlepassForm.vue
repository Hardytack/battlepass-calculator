<template>
  <section class="form-container">
    <form @submit.prevent>
      <div class="input-group">
        <label>Name</label>
        <input type="text" v-model.trim="name" placeholder="Battlepass Name" />
      </div>
      <div class="input-group">
        <label>Current XP</label>
        <input type="number" v-model.trim="currentXp" placeholder="0" />
      </div>
      <div class="input-group">
        <label>Goal XP</label>
        <input type="number" v-model.trim="totalXp" placeholder="35000" />
      </div>
      <div class="input-group">
        <label>End Date</label>
        <input type="date" v-model.trim="endDate" />
      </div>
      <div class="button-group" v-if="!username">
        <button @click="calculateXp">Calculate</button>
        <router-link to="/login"> <button>Login to Save!</button></router-link>
      </div>
      <div class="button-group" v-else>
        <button @click="calculateXp">Calculate</button>
        <button @click="saveData" :disabled="disabledButton">Save</button>
      </div>
      <p class="errorMessage">{{ errorMessage }}</p>
    </form>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "PassForm",
  data() {
    return {
      name: "",
      currentXp: null,
      totalXp: null,
      endDate: "",
      errorMessage: "",
      disabledButton: false,
    };
  },
  computed: {
    ...mapGetters(["username", "token"]),
    xpDifference() {
      return this.totalXp - this.currentXp;
    },
    daysLeft() {
      const targetDate = new Date(this.endDate);
      const todaysDate = new Date(Date.now());
      const differenceTime = targetDate.getTime() - todaysDate.getTime();
      const differenceDays = differenceTime / (1000 * 3600 * 24);
      return Math.ceil(differenceDays);
    },
  },
  methods: {
    calculateXp() {
      this.errorMessage = "";
      if (!this.name || !this.endDate || !this.currentXp || !this.totalXp)
        return (this.errorMessage = "Please fill out all fields");
      this.$emit("test-emit", {
        name: this.name,
        daysLeft: this.daysLeft,
        xpDifference: this.xpDifference,
        show: true,
      });
    },
    async saveData() {
      this.errorMessage = "";
      if (!this.name || !this.currentXp || !this.totalXp || !this.endDate) {
        return (this.errorMessage = "Please fill out all fields");
      }
      await fetch("http://127.0.0.1:5000/bp/user-bp", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          Authorization: `Bearer ${this.token}`,
        },
        body: JSON.stringify({
          name: this.name,
          currentXP: this.currentXp,
          totalXP: this.totalXp,
          endDate: this.endDate,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (!data.success) {
            this.errorMessage = data.message;
          } else {
            alert(data.message);
          }
        });
    },
    deleteData() {
      alert("Coming Soon");
    },
    getData() {
      alert("Coming Soon");
    },
  },
  beforeMount() {
    console.log("Coming Soon");
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
