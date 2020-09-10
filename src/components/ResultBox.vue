<template>
  <section id="result-box">
    <h2 id="result-header">You have {{ stats.days }} left</h2>
    <h3 id="result-subhead">You need {{ stats.xpDifference }}xp</h3>
    <h4 id="result-thirdhead">
      That's an average of {{ Math.floor(stats.xpDifference / stats.days) }}xp
      per day
    </h4>
  </section>
</template>

<script>
export default {
  name: "ResultBox",
  props: ["stats"],
};
</script>
