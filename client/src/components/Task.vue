<template>
  <div>
    <h3>{{ task.text }}</h3>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: ["task"]
};
</script>
<style lang="scss"></style>
