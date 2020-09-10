<template>
  <section id="result-box" :class="{visible: !stats.show}">
    <h2 id="result-header">You have {{ stats.daysLeft }} days left</h2>
    <h3 id="result-subhead">You need {{ stats.xpDifference }}xp</h3>
    <h4 id="result-thirdhead">
      That's an average of
      {{ Math.floor(stats.xpDifference / stats.daysLeft) }}xp per day
    </h4>
  </section>
</template>

<script>
export default {
  name: "ResultBox",
  props: ["stats"],
};
</script>

<style lang="scss">
.visible {
  display: none;
}
</style>
