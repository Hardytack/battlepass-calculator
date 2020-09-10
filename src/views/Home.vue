<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <Battlepass v-on:test-emit="handleEmit" />
    <ResultBox v-bind:stats="passData" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
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
    HelloWorld,
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
