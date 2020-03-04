<template>
  <div class="task">
    <h3>{{ task.text }}</h3>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: ["task"]
};
</script>
<style lang="scss">
.task {
  width: 80%;
  color: black;
  background-color: white;
  margin: 5px 10px;
  border-radius: 1rem;
}
</style>
