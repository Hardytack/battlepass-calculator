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
      <div class="button-group">
        <button @click="calculateXp">Calculate</button>
        <button @click="saveData">Save</button>
        <button @click="getData">Load</button>
        <button @click="deleteData">Delete</button>
      </div>
    </form>
  </section>
</template>

<script>
export default {
  name: "PassForm",
  data() {
    return {
      name: "",
      currentXp: null,
      totalXp: null,
      endDate: "",
    };
  },
  computed: {
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
      if (!this.name || !this.endDate)
        return alert("Please fill out all fields");
      this.$emit("test-emit", {
        name: this.name,
        daysLeft: this.daysLeft,
        xpDifference: this.xpDifference,
        show: true,
      });
    },
    saveData() {
      let data = {
        name: this.name,
        currentXp: this.currentXp,
        totalXp: this.totalXp,
        endDate: this.endDate,
      };
      localStorage.setItem("battlepass", JSON.stringify(data));
      alert("Data has been saved");
    },
    deleteData() {
      localStorage.removeItem("battlepass");
      alert("Data has been removed");
    },
    getData() {
      let data = JSON.parse(localStorage.getItem("battlepass"));
      if (!data) return alert("No data has been saved");
      this.name = data.name;
      this.currentXp = data.currentXp;
      this.totalXp = data.totalXp;
      this.endDate = data.endDate;
    },
  },
  beforeMount() {
    let data = JSON.parse(localStorage.getItem("battlepass"));
    if (!data) return;
    this.name = data.name;
    this.currentXp = data.currentXp;
    this.totalXp = data.totalXp;
    this.endDate = data.endDate;
    this.calculateXp();
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
