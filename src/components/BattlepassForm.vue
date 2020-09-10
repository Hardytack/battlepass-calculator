<template>
  <section class="form-container">
    <form @submit.prevent>
      <div class="input-group">
        <label>Name</label>
        <input type="text" v-model.trim="name" placeholder="Battlepass Name" />
      </div>
      <div class="input-group">
        <label>Current XP</label>
        <input type="number" v-model.trim="currentXp" placeholder="123" />
      </div>
      <div class="input-group">
        <label>Goal XP</label>
        <input type="number" v-model.trim="totalXp" />
      </div>
      <div class="input-group">
        <label>End Date</label>
        <input type="date" v-model.trim="endDate" />
      </div>
      <div class="input-group">
        <input type="submit" value="Calculate" @click="calculateXp" />
        <input type="submit" value="Save" @click="saveData" />
        <input type="submit" value="Load" @click="getData" />
      </div>
    </form>
    <button
      class="testbutton"
      @click="$emit('test-emit', { name, days: 27, xpDifference })"
    >
      Test
    </button>
  </section>
</template>

<script>
export default {
  name: "PassForm",
  data() {
    return {
      name: "",
      currentXp: 0,
      totalXp: 0,
      endDate: "",
    };
  },
  computed: {
    xpDifference() {
      return this.totalXp - this.currentXp;
    },
  },
  methods: {
    calculateXp() {
      console.log(`You need ${this.totalXp - this.currentXp}xp`);
    },
    saveData() {
      let data = {
        name: this.name,
        currentXp: this.currentXp,
        totalXp: this.totalXp,
        endDate: this.endDate,
      };
      localStorage.setItem("battlepass", JSON.stringify(data));
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
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
