<template>
  <section>
    <h1>Edit Coming Soon for id {{ $route.params.id }}</h1>
    <BattlepassForm name="Test Prop" />
  </section>
</template>

<script>
import BattlepassForm from "../components/BattlepassForm.vue";
export default {
  name: "EditPass",
  components: {
    BattlepassForm,
  },
};
</script>
