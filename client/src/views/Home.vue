<template>
  <div class="home">
    <Battlepass v-on:test-emit="handleEmit" />
    <ResultBox v-bind:stats="passData" />
  </div>
</template>

<script>
// @ is an alias to /src
import Battlepass from "@/components/BattlepassForm.vue";
import ResultBox from "@/components/ResultBox.vue";

export default {
  name: "Home",
  data() {
    return {
      passData: {},
    };
  },
  components: {
    Battlepass,
    ResultBox,
  },
  methods: {
    handleEmit(e) {
      this.passData = e;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
