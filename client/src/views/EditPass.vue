<template>
  <section>
    <h1>Currently Editing {{ name }}</h1>
    <BattlepassForm
      :name="name"
      :currentXp="currentXp"
      :totalXp="totalXp"
      :endDate="endDate"
      :editForm="true"
      :passID="$route.params.id"
      v-on:calc-emit="handleEmit"
    />
    <ResultBox :stats="passData" />
  </section>
</template>

<script>
import BattlepassForm from "../components/BattlepassForm.vue";
import ResultBox from "../components/ResultBox.vue";
export default {
  name: "EditPass",
  components: {
    BattlepassForm,
    ResultBox,
  },
  data() {
    return {
      passData: {},
      name: "",
      currentXp: null,
      totalXp: null,
      endDate: "",
    };
  },
  methods: {
    handleEmit(e) {
      this.passData = e;
    },
  },
  beforeCreate() {
    fetch(
      `${process.env.VUE_APP_URL}/bp/user-bp?bpid=${this.$route.params.id}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    )
      .then((res) => res.json())
      .then((data) => {
        this.name = data.passes[2];
        this.currentXp = data.passes[3];
        this.totalXp = data.passes[4];
        this.endDate = data.passes[5];
      });
  },
};
</script>
