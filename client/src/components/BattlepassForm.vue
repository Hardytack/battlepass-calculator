<template>
  <section class="form-container">
    <form @submit.prevent>
      <div class="input-group">
        <label>Name</label>
        <input
          type="text"
          v-model.trim="dataName"
          placeholder="Battlepass Name"
        />
      </div>
      <div class="input-group">
        <label>Current XP</label>
        <input type="number" v-model.trim="dataCurrentXp" placeholder="0" />
      </div>
      <div class="input-group">
        <label>Goal XP</label>
        <input type="number" v-model.trim="dataTotalXp" placeholder="35000" />
      </div>
      <div class="input-group">
        <label>End Date</label>
        <input type="date" v-model.trim="dataEndDate" />
      </div>
      <div class="button-group" v-if="!username">
        <button @click="calculateXp">Calculate</button>
        <router-link to="/login"> <button>Login to Save!</button></router-link>
      </div>
      <div class="button-group" v-else>
        <button @click="calculateXp">Calculate</button>
        <button @click="saveData" :disabled="disabledButton">Save</button>
      </div>
      <div class="single-button-group" v-if="username">
        <router-link to="/my-profile"
          ><button>
            Load A Saved Pass
          </button>
        </router-link>
      </div>
      <p class="errorMessage">{{ errorMessage }}</p>
    </form>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "PassForm",
  props: {
    name: {
      type: String,
      default: "",
    },
    currentXp: {
      type: Number,
      default: null,
    },
    totalXp: {
      type: Number,
      default: null,
    },
    endDate: {
      type: String,
      default: "",
    },
    editForm: {
      type: Boolean,
      default: false,
    },
    passID: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      dataName: this.name,
      dataCurrentXp: this.currentXp,
      dataTotalXp: this.totalXp,
      dataEndDate: this.endDate,
      errorMessage: "",
      disabledButton: false,
    };
  },
  watch: {
    name() {
      this.dataName = this.name;
      this.dataEndDate = this.endDate;
      this.dataCurrentXp = this.currentXp;
      this.dataTotalXp = this.totalXp;
    },
    deep: true,
  },
  computed: {
    getName: {
      get() {
        return this.name;
      },
      set() {},
    },
    ...mapGetters(["username", "token"]),
    xpDifference() {
      return this.dataTotalXp - this.dataCurrentXp;
    },
    daysLeft() {
      const targetDate = new Date(this.dataEndDate);
      const todaysDate = new Date(Date.now());
      const differenceTime = targetDate.getTime() - todaysDate.getTime();
      const differenceDays = differenceTime / (1000 * 3600 * 24);
      return Math.ceil(differenceDays);
    },
  },
  methods: {
    calculateXp() {
      this.errorMessage = "";
      if (
        !this.dataName ||
        !this.dataCurrentXp ||
        !this.dataTotalXp ||
        !this.dataEndDate
      )
        return (this.errorMessage = "Please fill out all fields");
      this.$emit("test-emit", {
        name: this.name,
        daysLeft: this.daysLeft,
        xpDifference: this.xpDifference,
        show: true,
      });
    },
    // Add check for new or update
    async saveData() {
      this.errorMessage = "";
      if (
        !this.dataName ||
        !this.dataCurrentXp ||
        !this.dataTotalXp ||
        !this.dataEndDate
      ) {
        return (this.errorMessage = "Please fill out all fields");
      }
      // Submits an update request if pass already existed
      if (this.editForm) {
        await fetch(`${process.env.VUE_APP_URL}/bp/user-bp`, {
          method: "PATCH",
          headers: {
            "content-type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
          body: JSON.stringify({
            name: this.dataName,
            currentXP: this.dataCurrentXp,
            totalXP: this.dataTotalXp,
            endDate: this.dataEndDate,
            id: this.passID,
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
      } else {
        await fetch(`${process.env.VUE_APP_URL}/bp/user-bp`, {
          method: "POST",
          headers: {
            "content-type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
          body: JSON.stringify({
            name: this.dataName,
            currentXP: this.dataCurrentXp,
            totalXP: this.dataTotalXp,
            endDate: this.dataEndDate,
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
      }
    },
    deleteData() {
      alert("Coming Soon");
    },
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/form-style.scss";
</style>
